from themes import *

NOMBRES = {"name": "Nombres", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "11", 12: "12", 13: "13", 14: "14", 15: "15", 16: "16", 17: "17", 18: "18", 19: "19", 20: "20", 21: "21", 22: "22", 23: "23", 24: "24",
           25: "25", 26: "26", 27: "27", 28: "28", 29: "29", 30: "30", 31: "31", 32: "32", 33: "33", 34: "34", 35: "35", 36: "36", 37: "37", 38: "38", 39: "39", 40: "40", 41: "41", 42: "42", 43: "43", 44: "44", 45: "45", 46: "46", 47: "47", 48: "48", 49: "49", 50: "50"}

DRAPEAUX = {"name": "Drapeaux", 1: "DrapeauUSA.png", 2: "DrapeauFrance.png", 3: "DrapeauQatar.png", 4: "DrapeauAfriqueDuSud.png", 5: "DrapeauVatican.png", 6: "DrapeauTuvalu.png", 7: "DrapeauLuxembourg.png", 8: "DrapeauNouvelleZelande.png", 9: "DrapeauAustralie.png", 10: "DrapeauSingapour.png", 11: "DrapeauTurquie.png", 12: "DrapeauTunisie.png", 13: "DrapeauMaroc.png", 14: "DrapeauAlgerie.png", 15: "DrapeauEgypte.png", 16: "DrapeauMyanmar.png", 17: "DrapeauBangladesh.png", 18: "DrapeauMongolie.png", 19: "DrapeauMonaco.png", 20: "DrapeauAndorre.png", 21: "DrapeauLituanie.png", 22: "DrapeauDanemark.png", 23: "DrapeauPaysBas.png", 24: "DrapeauBelgique.png", 25: "DrapeauGroeland.png",
            26: "DrapeauIslande.png", 27: "DrapeauChypre.png", 28: "DrapeauMalte.png", 29: "DrapeauKazakhstan.png", 30: "DrapeauInde.png", 31: "DrapeauCoreeDuNord.png", 32: "DrapeauCoreeDuSud.png", 33: "DrapeauChine.png", 34: "DrapeauJapon.png", 35: "DrapeauRussie.png", 36: "DrapeauUkraine.png", 37: "DrapeauRepubiqueTcheque.png", 38: "DrapeauAutriche.png", 39: "DrapeauPologne.png", 40: "DrapeauPortugal.png", 41: "DrapeauCanada.png", 42: "DrapeauArgentine.png", 43: "DrapeauBresil.png", 44: "DrapeauAllemagne.png", 45: "DrapeauNorvege.png", 46: "DrapeauFinlande.png", 47: "DrapeauSuede.png", 48: "DrapeauAngleterre.png", 49: "DrapeauEspagne.png", 50: "DrapeauItalie.png"}


def test_random_theme():
    for elt in random_theme(NOMBRES, 10):
        assert elt in list(NOMBRES.values())
    assert len(random_theme(NOMBRES, 10)) == 10
