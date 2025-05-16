from acceptance_rates import augment_acceptance_rates
from author_id_fixer import apply_author_fixes, recode_acmids
from orcid_backfill import backfill_orcid
from other_fixes import apply_other_fixes
from name_fixes import fix_names
from add_awards import add_awards
from affiliation_fixes import fix_affiliations

if __name__ == '__main__':
    augment_acceptance_rates()
    apply_author_fixes()
    recode_acmids()
    backfill_orcid()
    apply_other_fixes()
    fix_names()
    add_awards()
    fix_affiliations()
