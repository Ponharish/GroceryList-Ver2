from django import forms

class GroceryForm1(forms.Form):
    rocksalt_quantity = forms.CharField(max_length=100, required=False, initial='')
    fineslt_quantity = forms.CharField(max_length=100, required=False, initial='')
    turmeric_quantity = forms.CharField(max_length=100, required=False, initial='')
    brownsugar_quantity = forms.CharField(max_length=100, required=False, initial='')
    whitesugar_quantity = forms.CharField(max_length=100, required=False, initial='')
    uriddhall_quantity = forms.CharField(max_length=100, required=False, initial='')
    dhalluridsplit_quantity = forms.CharField(max_length=100, required=False, initial='')
    toordhall_quantity = forms.CharField(max_length=100, required=False, initial='')
    splitblackdhall_quantity = forms.CharField(max_length=100, required=False, initial='')
    bbengalgramdhall_quantity = forms.CharField(max_length=100, required=False, initial='')
    whitechanna_quantity = forms.CharField(max_length=100, required=False, initial='')
    peanut_quantity = forms.CharField(max_length=100, required=False, initial='')
    mustard_quantity = forms.CharField(max_length=100, required=False, initial='')
    pepper_quantity = forms.CharField(max_length=100, required=False, initial='')
    fenugreek_quantity = forms.CharField(max_length=100, required=False, initial='')
    rava_quantity = forms.CharField(max_length=100, required=False, initial='')
    idlyrice_quantity = forms.CharField(max_length=100, required=False, initial='')
    ponnirice_quantity = forms.CharField(max_length=100, required=False, initial='')
    basmatirice_quantity = forms.CharField(max_length=100, required=False, initial='')
    rawrice_quantity = forms.CharField(max_length=100, required=False, initial='')
    jeerarice_quantity = forms.CharField(max_length=100, required=False, initial='')
    idayamgingellyoil_quantity = forms.CharField(max_length=100, required=False, initial='')
    goldwinner_quantity = forms.CharField(max_length=100, required=False, initial='')
    coconutoil_quantity = forms.CharField(max_length=100, required=False, initial='')
    coldpressoil_quantity = forms.CharField(max_length=100, required=False, initial='')
    tamerind_quantity = forms.CharField(max_length=100, required=False, initial='')
    roastedgramdhall_quantity = forms.CharField(max_length=100, required=False, initial='')
    ragiflour_quantity = forms.CharField(max_length=100, required=False, initial='')
    moongdhall_quantity = forms.CharField(max_length=100, required=False, initial='')
    greanbean_quantity = forms.CharField(max_length=100, required=False, initial='')
    blackchanna_quantity = forms.CharField(max_length=100, required=False, initial='')
    motchaibean_quantity = forms.CharField(max_length=100, required=False, initial='')
    pappadam_quantity = forms.CharField(max_length=100, required=False, initial='')
    boost_quantity = forms.CharField(max_length=100, required=False, initial='')
    filtercoffee_quantity = forms.CharField(max_length=100, required=False, initial='')
    ajax_quantity = forms.CharField(max_length=100, required=False, initial='')
    hotwaterbag_quantity = forms.CharField(max_length=100, required=False, initial='')
    carrybag_quantity = forms.CharField(max_length=100, required=False, initial='')
    smallonion_quantity = forms.CharField(max_length=100, required=False, initial='')
    ghee_quantity = forms.CharField(max_length=100, required=False, initial='')
    cashewnut_quantity = forms.CharField(max_length=100, required=False, initial='')
    murukkuflour_quantity = forms.CharField(max_length=100, required=False, initial='')
    riceflour_quantity = forms.CharField(max_length=100, required=False, initial='')
    bengalgramflour_quantity = forms.CharField(max_length=100, required=False, initial='')
    cornflour_quantity = forms.CharField(max_length=100, required=False, initial='')
    maidaflour_quantity = forms.CharField(max_length=100, required=False, initial='')
    himalayashampoo_quantity = forms.CharField(max_length=100, required=False, initial='')
    gokulsandal_quantity = forms.CharField(max_length=100, required=False, initial='')
    gulabjamun_quantity = forms.CharField(max_length=100, required=False, initial='')
    aval_quantity = forms.CharField(max_length=100, required=False, initial='')
    jaggery_quantity = forms.CharField(max_length=100, required=False, initial='')
    citronpickle_quantity = forms.CharField(max_length=100, required=False, initial='')
    incense_quantity = forms.CharField(max_length=100, required=False, initial='')
    sambrani_quantity = forms.CharField(max_length=100, required=False, initial='')
    prayeroil_quantity = forms.CharField(max_length=100, required=False, initial='')
    panjuthiri_quantity = forms.CharField(max_length=100, required=False, initial='')
    sandalpowder_quantity = forms.CharField(max_length=100, required=False, initial='')
    vermicelli_quantity = forms.CharField(max_length=100, required=False, initial='')
    lg_quantity = forms.CharField(max_length=100, required=False, initial='')
    cummin_quantity = forms.CharField(max_length=100, required=False, initial='')
    fennelseed_quantity = forms.CharField(max_length=100, required=False, initial='')
    gooddaybiscuit_quantity = forms.CharField(max_length=100, required=False, initial='')
    bhelpuri_quantity = forms.CharField(max_length=100, required=False, initial='')
    cardamon_quantity = forms.CharField(max_length=100, required=False, initial='')
    bayleaf_quantity = forms.CharField(max_length=100, required=False, initial='')
    corienderseed_quantity = forms.CharField(max_length=100, required=False, initial='')
    javvarasi_quantity = forms.CharField(max_length=100, required=False, initial='')
    kodomillet_quantity = forms.CharField(max_length=100, required=False, initial='')
    littlemillet_quantity = forms.CharField(max_length=100, required=False, initial='')
    barnyardmillet_quantity = forms.CharField(max_length=100, required=False, initial='')
    mattarice_quantity = forms.CharField(max_length=100, required=False, initial='')
    muttonmasala_quantity = forms.CharField(max_length=100, required=False, initial='')


    notes = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))