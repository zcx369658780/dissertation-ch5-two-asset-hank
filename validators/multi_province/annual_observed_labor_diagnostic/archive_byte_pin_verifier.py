"""In-memory comparison with a caller-declared pin; no source authentication."""

from dataclasses import dataclass
import hashlib


@dataclass(frozen=True, slots=True)
class ArchiveBytePinDeclaration:
    role: str
    source_identifier: str
    source_path_label: str
    expected_length: int
    byte_cap: int
    expected_sha256: str

    def __post_init__(self) -> None:
        if type(self.role) is not str or self.role not in (
            "STATE_JSON", "FROZEN_SHARE_OPAQUE_NPZ"
        ):
            raise ValueError("DECLARATION_ROLE")
        for label in (self.source_identifier, self.source_path_label):
            if (
                type(label) is not str or not label.strip()
                or label.strip().upper() == "UNKNOWN"
            ):
                raise ValueError("DECLARATION_LABEL")
        if type(self.expected_length) is not int or self.expected_length <= 0:
            raise ValueError("DECLARATION_LENGTH")
        if type(self.byte_cap) is not int or self.byte_cap <= 0:
            raise ValueError("DECLARATION_CAP")
        if self.expected_length > self.byte_cap:
            raise ValueError("DECLARATION_LENGTH_CAP")
        pin = self.expected_sha256
        if type(pin) is not str or len(pin) != 64 or any(
            char not in "0123456789abcdefABCDEF" for char in pin
        ):
            raise ValueError("DECLARATION_PIN")


@dataclass(frozen=True, slots=True)
class ArchiveBytePinVerification:
    code: str
    role: str | None = None
    source_identifier: str | None = None
    source_path_label: str | None = None
    actual_size: int | None = None
    actual_sha256: str | None = None

    def __post_init__(self) -> None:
        if type(self) is not ArchiveBytePinVerification:
            raise ValueError("RESULT_TYPE")
        if type(self.code) is not str or self.code not in (
            "DECLARATION_TYPE", "PAYLOAD_TYPE", "CAP_EXCEEDED",
            "LENGTH_MISMATCH", "HASH_FAILURE", "SHA256_MISMATCH", "MATCH",
        ):
            raise ValueError("RESULT_CODE")
        if self.role is not None and (
            type(self.role) is not str
            or self.role not in ("STATE_JSON", "FROZEN_SHARE_OPAQUE_NPZ")
        ):
            raise ValueError("RESULT_ROLE")
        for label in (self.source_identifier, self.source_path_label):
            if label is not None and (
                type(label) is not str or not label.strip()
                or label.strip().upper() == "UNKNOWN"
            ):
                raise ValueError("RESULT_LABEL")
        if self.actual_size is not None and (
            type(self.actual_size) is not int or self.actual_size < 0
        ):
            raise ValueError("RESULT_SIZE")
        digest = self.actual_sha256
        if digest is not None and (
            type(digest) is not str or len(digest) != 64
            or any(char not in "0123456789abcdefABCDEF" for char in digest)
        ):
            raise ValueError("RESULT_PIN")

    @property
    def byte_identity_matches_declared_pin(self) -> bool:
        return self.code == "MATCH"

    @property
    def classification(self) -> str:
        return "ARCHIVE_DERIVED"

    @property
    def source_authenticated(self) -> bool:
        return False

    @property
    def original_live_identity_restored(self) -> bool:
        return False

    @property
    def scientific_validity_established(self) -> bool:
        return False

    @property
    def model_activation(self) -> bool:
        return False

    @property
    def execution_admitted(self) -> bool:
        return False


def verify_archive_byte_pin(
    declaration: ArchiveBytePinDeclaration, payload: bytes
) -> ArchiveBytePinVerification:
    """Compare exact immutable bytes without retaining or interpreting payload."""
    if type(declaration) is not ArchiveBytePinDeclaration:
        return ArchiveBytePinVerification("DECLARATION_TYPE")

    def result(
        code: str, size: int | None = None, digest: str | None = None
    ) -> ArchiveBytePinVerification:
        return ArchiveBytePinVerification(
            code, declaration.role, declaration.source_identifier,
            declaration.source_path_label, size, digest,
        )

    if type(payload) is not bytes:
        return result("PAYLOAD_TYPE")
    size = len(payload)
    if size > declaration.byte_cap:
        return result("CAP_EXCEEDED", size)
    if size != declaration.expected_length:
        return result("LENGTH_MISMATCH", size)
    try:
        digest = hashlib.sha256(payload).hexdigest()
    except Exception:
        return result("HASH_FAILURE", size)
    if digest.lower() != declaration.expected_sha256.lower():
        return result("SHA256_MISMATCH", size, digest)
    return result("MATCH", size, digest)
