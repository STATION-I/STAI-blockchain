from dataclasses import dataclass
from typing import List, Optional, Tuple

from staicoin.types.blockchain_format.program import Program
from staicoin.types.blockchain_format.sized_bytes import bytes32
from staicoin.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class CCInfo(Streamable):
    my_genesis_checker: Optional[Program]  # this is the program
    lineage_proofs: List[Tuple[bytes32, Optional[Program]]]  # {coin.name(): lineage_proof}
