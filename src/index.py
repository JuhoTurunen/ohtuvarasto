from varasto import Varasto


def huono_testi():
    print("\nVirhetilanteita:")
    huono = Varasto(-100.0)
    print(huono, "\nVarasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print(
        "Luonnin jälkeen:\nMehuvarasto:",
        mehua,
        "\nOlutvarasto:",
        olutta,
        "\n\nOlut getterit:\nsaldo =",
        olutta.saldo,
        "\ntilavuus =",
        olutta.tilavuus,
        "\npaljonko_mahtuu =",
        olutta.paljonko_mahtuu(),
        "\nMehu setterit:\nLisätään 50.7",
    )
    mehua.lisaa_varastoon(50.7)
    print("Mehuvarasto:", mehua, "\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print("Mehuvarasto:", mehua)

    huono_testi()

    print("\nOlutvarasto:", olutta, "\nolutta.lisaa_varastoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(
        "Olutvarasto:", olutta, 
        "\nMehuvarasto:", mehua, 
        "\n\nmehua.lisaa_varastoon(-666.0)",
    )
    mehua.lisaa_varastoon(-666.0)
    print(
        "Mehuvarasto:",
        mehua,
        "\nOlutvarasto:",
        olutta,
        "\n\nolutta.ota_varastosta(1000.0)",
        "\nsaatiin",
        olutta.ota_varastosta(1000.0),
        "\nOlutvarasto:",
        olutta,
        "\nMehuvarasto:",
        mehua,
        "\nmehua.ota_varastosta(-32.9)",
        "\nsaatiin",
        mehua.ota_varastosta(-32.9),
        "\nMehuvarasto:",
        mehua,
    )


if __name__ == "__main__":
    main()
