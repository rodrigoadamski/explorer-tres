import requests
from django.shortcuts import render

def tide_view(request):
    cidade = request.GET.get('cidade', 'Natal')
    url = f"https://api.example.com/mare?city={cidade}"  # Substitua pela API real

    try:
        response = requests.get(url)
        data = response.json()  # Supondo que retorne JSON

        # Normaliza a chave 'marés' para 'mares'
        if 'marés' in data:
            data['mares'] = data.pop('marés')
    except Exception as e:
        data = {"error": str(e)}

    return render(request, 'tide/tide.html', {'data': data, 'cidade': cidade})