# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    currency_rate_amount = fields.Float(
        string="Rate amount", compute="_compute_currency_rate_amount", digits=0,
    )
    show_currency_rate_amount = fields.Boolean(
        compute="_compute_show_currency_rate_amount", readonly=True
    )

    @api.depends(
        "state",
        "date",
        "line_ids.amount_currency",
        "company_id",
        "currency_id",
        "show_currency_rate_amount",
    )
    def _compute_currency_rate_amount(self):
        """ It's necessary to define value according to some cases:
        - Case A: Currency is equal to company currency (Value = 1)
        - Case B: Move exist previously (posted) and get real rate according to lines
        - Case C: Get expected rate (according to date) to show some value in creation.
        """
        self.currency_rate_amount = 1
        for item in self.filtered("show_currency_rate_amount"):
            lines = item.line_ids.filtered(lambda x: x.amount_currency > 0)
            if item.state == "posted" and lines:
                amount_currency_positive = sum(lines.mapped("amount_currency"))
                total_debit = sum(lines.mapped("debit"))
                item.currency_rate_amount = item.currency_id.round(
                    amount_currency_positive / total_debit
                )
            else:
                rates = item.currency_id._get_rates(item.company_id, item.date)
                item.currency_rate_amount = rates.get(item.currency_id.id)

    @api.depends("currency_id", "currency_id.rate_ids", "company_id")
    def _compute_show_currency_rate_amount(self):
        for item in self:
            item.show_currency_rate_amount = (
                item.currency_id and item.currency_id != item.company_id.currency_id
            )


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # TODO: This field should be removed in V16 as it is already
    # added by Odoo in the account module
    currency_rate_amount = fields.Float(
        string="Rate amount", compute="_compute_currency_rate_amount", digits=0,
    )

    @api.depends(
        "move_id.state",
        "move_id.date",
        "amount_currency",
        "debit",
        "move_id.company_id",
        "currency_id",
    )
    def _compute_currency_rate_amount(self):
        """ It's necessary to define value according to some cases:
        - Case A: Currency is equal to company currency (Value = 1)
        - Case B: Move exist previously (posted) and get real rate according to lines
        - Case C: Get expected rate (according to date) to show some value in creation.
        """
        # TODO: This method should be removed in V16 as the logic is
        # already added by Odoo in the account module
        self.currency_rate_amount = 1
        for item in self:
            if (
                not item.currency_id
                or item.currency_id == item.move_id.company_id.currency_id
            ):
                continue
            if item.move_id.state == "posted" and item.amount_currency > 0:
                item.currency_rate_amount = item.currency_id.round(
                    item.amount_currency / item.debit
                )
            else:
                rates = item.currency_id._get_rates(
                    item.move_id.company_id, item.move_id.date
                )
                item.currency_rate_amount = rates.get(item.currency_id.id)
