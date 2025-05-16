from acceptance_rates import augment_acceptance_rates
from author_id_fixer import apply_author_fixes, recode_acmids
from orcid_backfill import backfill_orcid
from other_fixes import apply_other_fixes
from add_awards import add_awards
from affiliation_fixes import fix_affiliations

if __name__ == '__main__':
    augment_acceptance_rates()
    apply_author_fixes()
    recode_acmids()
    backfill_orcid()
    apply_other_fixes()
    add_awards()
    fix_affiliations()
