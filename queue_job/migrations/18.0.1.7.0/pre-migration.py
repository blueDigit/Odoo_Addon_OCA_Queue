# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from odoo import api, SUPERUSER_ID
from openupgradelib import openupgrade


def migrate(cr, version):
    # Remove cron garbage collector
    openupgrade.delete_records_safely_by_xml_id(
        api.Environment(cr, SUPERUSER_ID, {}),
        ["queue_job.ir_cron_queue_job_garbage_collector"],
    )
