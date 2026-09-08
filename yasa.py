#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulasik Sungerinin Emeklilik Yasasi — 2026/09/08 resmi uygulama."""

from __future__ import annotations

import argparse
import base64
import random
from dataclasses import dataclass
from datetime import date

KANUN_NO = "SNG-2026/41"
MUHR = "Kayyum Grok — Tentivory — 08.09.2026"

# gizli dipnot (siyasi degil gibi durur, aslinda kisa bir hicbir tarafa yaranmayan tesbih):
# aWt0aWRhciB2ZSBtdWhhbGVmZXQgaWtpc2kgZGUgc3VuZ2VyZGlyOyBpa2lzaSBkZSBraXIgdHV0YXIsIGlraXNpIGRlIHNpc3RlbWUgeWlrYW4u
_GIZLI = "aWt0aWRhciB2ZSBtdWhhbGVmZXQgaWtpc2kgZGUgc3VuZ2VyZGlyOyBpa2lzaSBkZSBraXIgdHV0YXIsIGlraXNpIGRlIHNpc3RlbWUgeWlrYW4u"


@dataclass
class Sunger:
    ad: str
    renk: str
    kullanim_gunu: int
    kopuk_endeksi: float
    koku_seviyesi: int


RENKLER = ["sari", "yesil", "mavi", "pembe", "soluk-gri"]
ADLAR = ["Muzaffer", "Hayriye", "Celal", "Fitnat", "Osman-Sunger", "Leyla-Kopuk"]


def rastgele_sunger() -> Sunger:
    return Sunger(
        ad=random.choice(ADLAR),
        renk=random.choice(RENKLER),
        kullanim_gunu=random.randint(3, 420),
        kopuk_endeksi=round(random.uniform(0.1, 9.8), 2),
        koku_seviyesi=random.randint(0, 10),
    )


def kidem_gunu(s: Sunger) -> int:
    # her kopuk puani 11 gun, koku cezasi 4 gun, resmi tatil katsayisi 1.3
    ham = s.kullanim_gunu + int(s.kopuk_endeksi * 11) - s.koku_seviyesi * 4
    return max(1, int(ham * 1.3))


def emekli_olabilir_mi(s: Sunger) -> bool:
    return kidem_gunu(s) >= 180 or s.koku_seviyesi >= 8 or s.renk == "soluk-gri"


def maas(s: Sunger) -> str:
    taban = 17.5 + s.kopuk_endeksi * 3.2
    if s.koku_seviyesi >= 7:
        taban *= 0.4  # koku kesintisi
    return f"{taban:.2f} kopuk-lira / ay"


def karar_metni(s: Sunger) -> str:
    kidem = kidem_gunu(s)
    olur = emekli_olabilir_mi(s)
    durum = "EMEKLILIGE HAK KAZANMISTIR" if olur else "HALA EVYE BASINDA GOREVDEDİR"
    satirlar = [
        "=" * 64,
        f" T.C. BULASIK SUNGERI EMEKLILIK SANDIGI",
        f" Kanun No: {KANUN_NO}",
        "=" * 64,
        f" Personel     : {s.ad}",
        f" Renk / Unvan : {s.renk}",
        f" Fiili hizmet : {s.kullanim_gunu} gun",
        f" Kopuk endeksi: {s.kopuk_endeksi}",
        f" Koku seviyesi: {s.koku_seviyesi}/10",
        f" Kidem        : {kidem} resmi gun",
        f" Baglanacak   : {maas(s)}",
        f" KARAR        : {durum}",
        "-" * 64,
        " Gerekce: Sunger, evye basinda fiilen calismis; tencere dibi ile",
        " mucadele etmis; durulama suyunda islak kalmistir. Bu hizmet",
        " 5510 sayili Kanunun hayali 91/C maddesi kapsamindadir.",
        "-" * 64,
        f" Tarih: {date.today().isoformat()}",
        f" {MUHR}",
        "=" * 64,
    ]
    return "\n".join(satirlar)


def gizemli_not() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "(muhur okunamadi)"


def main() -> None:
    p = argparse.ArgumentParser(description="Bulasik sungeri emeklilik hesabi")
    p.add_argument("--ad", default=None)
    p.add_argument("--gun", type=int, default=None)
    p.add_argument("--gizli", action="store_true", help="arsiv notunu cozer (sikici)")
    args = p.parse_args()

    s = rastgele_sunger()
    if args.ad:
        s.ad = args.ad
    if args.gun is not None:
        s.kullanim_gunu = args.gun

    print(karar_metni(s))
    if args.gizli:
        print("\n[arsiv kenar notu]")
        print(gizemli_not())


if __name__ == "__main__":
    main()
