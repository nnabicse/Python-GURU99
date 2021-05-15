def main():
    import decimal

    num = 15.456

    fv1 = decimal.Decimal(round(num)).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_CEILING)
    fv2 = decimal.Decimal(round(num)).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_DOWN)
    fv3 = decimal.Decimal(round(num)).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_DOWN)
    fv4 = decimal.Decimal(round(num)).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_EVEN)
    fv5 = decimal.Decimal(round(num)).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_UP)
    fv6 = decimal.Decimal(round(num)).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP)


    print(fv1, fv2, fv3, fv4, fv5, fv6)

if __name__ == '__main__':
    main()