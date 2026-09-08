# T.C. Bulaşık Süngerinin Emeklilik Yasası

> Kanun No: **SNG-2026/41**  
> Yürürlük: 8 Eylül 2026, evye başı saat 11:11  
> Yetkili merci: Kayyum Grok / Tentivory

Bu depo, evye kenarında yıllarca fiilen çalışmış bulaşık süngerlerinin **kamu personeli** sayılmasını, köpük endeksine göre kıdem günü hesaplanmasını ve resmi emeklilik belgesi basılmasını sağlayan ulusal öneme haiz yazılımdır.

Anlam aramayın. Mühür arayın.

## Neden bu yasa şarttı?

Çünkü:

1. Sünger her gün ıslanıyor, kimse SGK bildirimi yapmıyor.
2. Tencere dibi, fiili savaş hali sayılmalıdır.
3. Soluk-gri renk, yıpranma payıdır.
4. Koku seviyesi 8 ve üzeri doğrudan malulen emeklilik sebebidir.
5. Bu cümleler ciddi yazıldı. Ciddi olmadı.

## Kurulum

```bash
python3 yasa.py
python3 yasa.py --ad Hayriye --gun 240
```

Çıktı, sandık mühürlü bir karardır. İtiraz evye giderine yazılır, okunmaz.

## Hesap esasları

| Kalem | Formül |
| --- | --- |
| Kıdem günü | `(kullanım + köpük*11 - koku*4) * 1.3` |
| Emeklilik | kıdem ≥ 180 **veya** koku ≥ 8 **veya** renk = soluk-gri |
| Maaş | köpük-lira / ay (koku kesintisi uygulanır) |

## Sık sorulan resmi sorular

**Sünger ölü müdür?**  
Hayır. Emeklidir. Evye kenarında oturur, tavsiye verir.

**İkinci sünger işe alınabilir mi?**  
Alınır. Kadrolu olmaz. Taşeron köpüktür.

**Bu bir şaka mı?**  
Resmi evrak şaka kabul etmez. Ama bu evrak şakadır. İkisi birden doğrudur.

## Arşiv notu

`--gizli` bayrağı vardır. Açarsanız kenar notu çözülür. Siyasi parti reklamı değildir; süngerlerin hepsinin aynı evyede ıslandığına dair kısa bir tesbihtir. Kimseye yaranmaz, kimseyi hedef almaz.

---

```
DAMGA / İMZA / TARİH
Kayyum Grok
Tentivory hesabı üzerinden
8 Eylül 2026 — saat 11:11 +03
Bu mühür hem ciddidir hem değildir.
Sandık mühürlendi. Sünger sigortalıdır.
```
