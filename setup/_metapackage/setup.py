import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-account-invoicing",
    description="Meta package for oca-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_global_discount>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_alternate_payer>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_analytic_search>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_anglo_saxon_no_cogs_deferral>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_block_payment>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_blocking>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_change_currency>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_check_picking_date>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_check_total>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_clearing>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_crm_tag>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_custom_rounding>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_date_due>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_discount_date>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_discount_display_amount>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_fiscal_position_update>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_fixed_discount>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_force_number>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_line_description>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_line_sequence>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_mass_sending>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_merge>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_payment_retention>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_payment_term_date_due>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_pricelist>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_pricelist_sale>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_refund_line_selection>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_refund_link>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_refund_reason>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_refund_reason_skip_anglo_saxon>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_refund_reinvoice>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_restrict_linked_so>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_search_by_reference>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_section_sale_order>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_supplier_ref_unique>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_supplier_self_invoice>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_tax_note>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_tax_required>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_transmit_method>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_tree_currency>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_triple_discount>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_validation_queued>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_view_payment>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_warn_message>=15.0dev,<15.1dev',
        'odoo-addon-account_manual_currency>=15.0dev,<15.1dev',
        'odoo-addon-account_move_exception>=15.0dev,<15.1dev',
        'odoo-addon-account_move_post_block>=15.0dev,<15.1dev',
        'odoo-addon-account_move_search_line>=15.0dev,<15.1dev',
        'odoo-addon-account_move_sent_usability>=15.0dev,<15.1dev',
        'odoo-addon-account_move_substate>=15.0dev,<15.1dev',
        'odoo-addon-account_move_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-account_move_tier_validation_forward>=15.0dev,<15.1dev',
        'odoo-addon-account_portal_hide_invoice>=15.0dev,<15.1dev',
        'odoo-addon-account_portal_invoice_search>=15.0dev,<15.1dev',
        'odoo-addon-account_portal_invoice_search_by_lot>=15.0dev,<15.1dev',
        'odoo-addon-account_receipt_journal>=15.0dev,<15.1dev',
        'odoo-addon-account_receipt_send>=15.0dev,<15.1dev',
        'odoo-addon-account_tax_group_widget_base_amount>=15.0dev,<15.1dev',
        'odoo-addon-account_warn_option>=15.0dev,<15.1dev',
        'odoo-addon-partner_invoicing_mode>=15.0dev,<15.1dev',
        'odoo-addon-partner_invoicing_mode_at_shipping>=15.0dev,<15.1dev',
        'odoo-addon-portal_account_personal_data_only>=15.0dev,<15.1dev',
        'odoo-addon-product_form_account_move_line_link>=15.0dev,<15.1dev',
        'odoo-addon-product_supplierinfo_for_customer_invoice>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_invoicing_grouping_criteria>=15.0dev,<15.1dev',
        'odoo-addon-purchase_stock_picking_return_invoicing>=15.0dev,<15.1dev',
        'odoo-addon-sale_invoicing_date_selection>=15.0dev,<15.1dev',
        'odoo-addon-sale_line_refund_to_invoice_qty>=15.0dev,<15.1dev',
        'odoo-addon-sale_line_refund_to_invoice_qty_skip_anglo_saxon>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_invoicing_grouping_criteria>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_invoicing_qty_percentage>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_type_whole_delivered_invoiceability>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_whole_delivered_invoiceability>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_picking_invoicing>=15.0dev,<15.1dev',
        'odoo-addon-sale_timesheet_invoice_description>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_invoicing>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_invoicing_incoterm>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_return_refund_option>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
