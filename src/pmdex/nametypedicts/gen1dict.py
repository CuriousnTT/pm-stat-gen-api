import re

base_data_string = "BulbasaurIvysaurVenusaurCharmanderCharmeleonCharizardSquirtleWartortleBlastoiseCaterpieMetapodButterfreeWeedleKakunaBeedrillPidgeyPidgeottoPidgeotRattataRaticateSpearowFearowEkansArbokPikachuRaichuSandshrewSandslashNidoran♀NidorinaNidoqueenNidoran♂NidorinoNidokingClefairyClefableVulpixNinetalesJigglypuffWigglytuffZubatGolbatOddishGloomVileplumeParasParasectVenonatVenomothDiglettDugtrioMeowthPersianPsyduckGolduckMankeyPrimeapeGrowlitheArcaninePoliwagPoliwhirlPoliwrathAbraKadabraAlakazamMachopMachokeMachampBellsproutWeepinbellVictreebelTentacoolTentacruelGeodudeGravelerGolemPonytaRapidashSlowpokeSlowbroMagnemiteMagnetonFarfetch'dDoduoDodrioSeelDewgongGrimerMukShellderCloysterGastlyHaunterGengarOnixDrowzeeHypnoKrabbyKinglerVoltorbElectrodeExeggcuteExeggutorCuboneMarowakHitmonleeHitmonchanLickitungKoffingWeezingRhyhornRhydonChanseyTangelaKangaskhanHorseaSeadraGoldeenSeakingStaryuStarmieMr. MimeScytherJynxElectabuzzMagmarPinsirTaurosMagikarpGyaradosLaprasDittoEeveeVaporeonJolteonFlareonPorygonOmanyteOmastarKabutoKabutopsAerodactylSnorlaxArticunoZapdosMoltresDratiniDragonairDragoniteMewtwoMew"
list_with_Mime_error = re.findall('[A-Z][^A-Z]*', base_data_string)
index_of_Mr = list_with_Mime_error.index('Mr. ')
index_of_Mime = list_with_Mime_error.index('Mime')
gen_one_list = list_with_Mime_error[:index_of_Mr] + [
    'Mr. Mime'
    ] + list_with_Mime_error[index_of_Mime+1:]
def checkDexProgress():
    print(gen_one_list)