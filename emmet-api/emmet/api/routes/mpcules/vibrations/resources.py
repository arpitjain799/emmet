from maggma.api.resource import ReadOnlyResource
from emmet.core.molecules.vibration import VibrationDoc

from maggma.api.query_operator import PaginationQuery, SortQuery, SparseFieldsQuery

from emmet.api.routes.mpcules.molecules.query_operators import (
    MultiMPculeIDQuery,
    ExactCalcMethodQuery,
    FormulaQuery,
    ChemsysQuery,
    ElementsQuery,
    ChargeSpinQuery,
)
from emmet.api.routes.mpcules.utils import MultiPropertyIDQuery
from emmet.api.core.settings import MAPISettings
from emmet.api.core.global_header import GlobalHeaderProcessor


def vibration_resource(vibes_store):
    resource = ReadOnlyResource(
        vibes_store,
        VibrationDoc,
        query_operators=[
            MultiMPculeIDQuery(),
            ExactCalcMethodQuery(),
            FormulaQuery(),
            ChemsysQuery(),
            ElementsQuery(),
            ChargeSpinQuery(),
            MultiPropertyIDQuery(),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(VibrationDoc, default_fields=["molecule_id", "property_id", "solvent", "last_updated"]),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["MPcules Vibrations"],
        sub_path="/vibrations/",
        disable_validation=True,
        timeout=MAPISettings(DB_VERSION="").TIMEOUT,
    )

    return resource
