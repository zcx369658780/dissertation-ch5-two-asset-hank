"""Prepared NumPy delivery for an inert annual seam; no scientific consumers."""
from dataclasses import dataclass, field
from pathlib import Path
import sys

import numpy as np


CANONICAL_PROVINCE_MAPPING = (
    (1, '北京市', '北京'), (2, '天津市', '天津'), (3, '河北省', '河北'),
    (4, '山西省', '山西'), (5, '内蒙古自治区', '内蒙古'),
    (6, '辽宁省', '辽宁'), (7, '吉林省', '吉林'), (8, '黑龙江省', '黑龙江'),
    (9, '上海市', '上海'), (10, '江苏省', '江苏'), (11, '浙江省', '浙江'),
    (12, '安徽省', '安徽'), (13, '福建省', '福建'), (14, '江西省', '江西'),
    (15, '山东省', '山东'), (16, '河南省', '河南'), (17, '湖北省', '湖北'),
    (18, '湖南省', '湖南'), (19, '广东省', '广东'), (20, '广西壮族自治区', '广西'),
    (21, '海南省', '海南'), (22, '重庆市', '重庆'), (23, '四川省', '四川'),
    (24, '贵州省', '贵州'), (25, '云南省', '云南'), (26, '西藏自治区', '西藏'),
    (27, '陕西省', '陕西'), (28, '甘肃省', '甘肃'), (29, '青海省', '青海'),
    (30, '宁夏回族自治区', '宁夏'), (31, '新疆维吾尔自治区', '新疆'),
)
_PREPARED_ARRAY = object()


def _validate_context(context, **metadata):
    module = sys.modules.get(type(context).__module__)
    expected = Path(__file__).with_name('annual_observed_labor_context.py').resolve()
    if (module is None or getattr(module, 'AnnualContext', None) is not type(context)
            or Path(getattr(module, '__file__', '')).resolve() != expected):
        raise ValueError('exact engineering annual context type required')
    module.AnnualContext.validate(context, **metadata)


def _mapping(province_mapping, province_axis, input_kind):
    if type(province_mapping) is not tuple or len(province_mapping) != len(province_axis):
        raise ValueError('explicit immutable full-name/model-name mapping required')
    if any(type(row) is not tuple or len(row) != 3 or type(row[0]) is not int
           or row[0] < 1 or type(row[1]) is not str or not row[1]
           or type(row[2]) is not str or not row[2] for row in province_mapping):
        raise ValueError('invalid provincial mapping')
    if any(len({row[k] for row in province_mapping}) != len(province_mapping)
           for k in range(3)):
        raise ValueError('duplicate provincial mapping')
    if tuple((i, full) for i, full, _ in province_mapping) != province_axis:
        raise ValueError('mapping must preserve exact annual index/source-name order')
    if input_kind == 'observed' and province_mapping != CANONICAL_PROVINCE_MAPPING:
        raise ValueError('observed mapping must preserve original canonical model names')
    if input_kind == 'synthetic':
        real_names = {name for row in CANONICAL_PROVINCE_MAPPING for name in row[1:]}
        if any(full in real_names or short in real_names for _, full, short in province_mapping):
            raise ValueError('synthetic mapping requires explicitly invented names')
    return province_mapping


@dataclass(frozen=True)
class _ArraySeal:
    carrier: object
    annual_context: object
    context_seal: object
    coefficients: tuple
    metadata: tuple
    province_mapping: tuple
    master: object
    backing_bytes: bytes


@dataclass(frozen=True)
class AnnualArrayCarrier:
    annual_context: object
    province_mapping: tuple
    province_order: tuple
    phi_destination_origin: object
    backing_bytes: bytes
    _preparation_token: object = field(default=None, repr=False, compare=False)
    _seal: object = field(default=None, init=False, repr=False, compare=False)

    def __post_init__(self):
        if self._preparation_token is not _PREPARED_ARRAY:
            raise ValueError('array carrier must originate at explicit annual preparation')

    def validate(self, *, annual_context, target_year, province_axis, source_sha256,
                 input_kind, price_basis, price_verified, province_mapping):
        if type(self) is not AnnualArrayCarrier or self._preparation_token is not _PREPARED_ARRAY:
            raise ValueError('exact prepared annual array carrier required')
        metadata = (target_year, province_axis, source_sha256, input_kind,
                    price_basis, price_verified)
        seal = self._seal
        if (type(seal) is not _ArraySeal or seal.carrier is not self
                or self.annual_context is not annual_context
                or seal.annual_context is not annual_context
                or seal.context_seal is not annual_context._seal
                or seal.metadata != metadata
                or seal.province_mapping != self.province_mapping
                or province_mapping != self.province_mapping
                or seal.master is not self.phi_destination_origin
                or seal.backing_bytes is not self.backing_bytes
                or seal.coefficients is not annual_context.phi_destination_origin):
            raise ValueError('annual array preparation seal mismatch')
        _validate_context(annual_context, target_year=target_year, province_axis=province_axis,
            source_sha256=source_sha256, input_kind=input_kind,
            price_basis=price_basis, price_verified=price_verified)
        _mapping(province_mapping, province_axis, input_kind)
        if self.province_order != tuple(short for _, _, short in province_mapping):
            raise ValueError('model short-name order mismatch')
        master = self.phi_destination_origin
        n = len(province_axis)
        if (type(master) is not np.ndarray or master.dtype != np.dtype(np.float64)
                or master.shape != (n, n) or master.strides != (n * 8, 8)
                or not master.flags.c_contiguous or master.flags.writeable
                or type(self.backing_bytes) is not bytes or len(self.backing_bytes) != n * n * 8):
            raise ValueError('float64 C-order immutable delivery required')
        # Every ndarray base must be read-only, ending at this exact immutable owner.
        base = master
        while type(base) is np.ndarray:
            if base.flags.writeable:
                raise ValueError('mutable delivery backing refused')
            base = base.base
        if base is not self.backing_bytes:
            raise ValueError('exact immutable bytes owner required')
        if master.tobytes(order='C') != self.backing_bytes or any(
                float(master[j, i]) != seal.coefficients[j][i]
                for j in range(n) for i in range(n)):
            raise ValueError('delivery must match exact annual tuple authority')


def prepare_annual_array(context, *, target_year, province_axis, source_sha256,
                         input_kind, price_basis, price_verified, province_mapping):
    """Prepare once, then explicitly reuse this sealed delivery for same-year turns.

    This array preparation conveys no permission to invoke production consumers.
    """
    _validate_context(context, target_year=target_year, province_axis=province_axis,
        source_sha256=source_sha256, input_kind=input_kind,
        price_basis=price_basis, price_verified=price_verified)
    mapping = _mapping(province_mapping, province_axis, input_kind)
    n = len(province_axis)
    backing = np.asarray(context.phi_destination_origin, dtype=np.float64,
                         order='C').tobytes(order='C')
    master = np.frombuffer(backing, dtype=np.float64).reshape((n, n))
    result = AnnualArrayCarrier(context, mapping, tuple(row[2] for row in mapping),
        master, backing, _preparation_token=_PREPARED_ARRAY)
    metadata = (target_year, province_axis, source_sha256, input_kind,
                price_basis, price_verified)
    object.__setattr__(result, '_seal', _ArraySeal(result, context, context._seal,
        context.phi_destination_origin, metadata, mapping, master, backing))
    AnnualArrayCarrier.validate(result, annual_context=context, target_year=target_year,
        province_axis=province_axis, source_sha256=source_sha256, input_kind=input_kind,
        price_basis=price_basis, price_verified=price_verified, province_mapping=mapping)
    return result
