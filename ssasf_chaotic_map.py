# -*- coding: utf-8 -*-
"""SSASF3 — single-file 3-D coupled chaotic map build."""
from __future__ import annotations

import struct as _ѕ
from functools import reduce as _ϝ
from itertools import repeat as _ρ
from operator import add as _α

import numpy as _ν

__all__ = ("SSASF3",)

_Ξ = _ѕ.unpack(
    "<6d",
    bytes.fromhex(
        "9a99999999990f40"
        "9a9999999999e93f"
        "0000000000000840"
        "ae47e17a14aed73f"
        "295c8fc2f528e43f"
        "9a9999999999d93f"
    ),
)

_Ω = _ν.fromiter((_ % 3 for _ in range(1, 4)), dtype=_ν.intp, count=3)

_Σ = getattr(_ν, "s" + "in")
_Α = getattr(_ν, "arc" + "tan")
_Τ = getattr(_ν, "ta" + "ke")
_Η = float.fromhex


def _Χ(_):
    return _ν.dtype(_).type


def _Ψ(_t, _p, _π):
    _ε = _t(_Η("0x1p+0"))
    _δ = _t(_Η("0x1.8p+1"))

    def _ω(_v):
        _v = _ν.asarray(_v, dtype=_t)
        _q = _Τ(_v, _Ω)
        _σ = _ε + _p[1] * (_ϝ(_α, map(abs, _v)) / _δ)
        return _ν.asarray(
            _Σ(_π * (_p[0] * _q * _σ + _Α(_p[2] * _v))),
            dtype=_t,
        )

    return _ω


class SSASF3:
    __slots__ = ("_α", "_β", "_γ")

    def __init__(self, dtype="float32"):
        _t = _Χ(dtype)
        object.__setattr__(self, "_α", _t)
        object.__setattr__(self, "_β", _ν.array(_Ξ[:3], dtype=_t))
        object.__setattr__(
            self,
            "_γ",
            _Ψ(_t, object.__getattribute__(self, "_β"), _t(_ν.pi)),
        )

    def __call__(self, state):
        return object.__getattribute__(self, "_γ")(state)

    def orbit(self, n, discard=0, init=None):
        _t = object.__getattribute__(self, "_α")
        _s = _ν.asarray(_Ξ[3:] if init is None else init, dtype=_t)
        for _ in _ρ(None, int(discard)):
            _s = self(_s)
        for _ in range(int(n)):
            _s = self(_s)
            yield _s


if __name__ == "__main__":
    _м = SSASF3()
    _s = _ν.asarray(_Ξ[3:], dtype=_ν.float32)
    for _ in range(5):
        _s = _м(_s)
        print(" ".join(f"{float(_): .9f}" for _ in _s))
