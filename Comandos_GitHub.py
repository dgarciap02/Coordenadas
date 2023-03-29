dicc={
  "success": True,
  "error": None,
  "data": [
{
      "object": "M",
      "confidence": "0.9740685",
      "detections": [
        0.49959216965742254,
        0.47045951859956237,
        0.2634584013050571,
        0.35667396061269147
      ]
    },
    {
      "object": "3",
      "confidence": "0.9456041",
      "detections": [
        0.7084013050570962,
        0.4458424507658643,
        0.20636215334420882,
        0.29431072210065645
      ]
    },
    {
      "object": "8",
      "confidence": "0.9413285",
      "detections": [
        0.6121533442088092,
        0.44803063457330417,
        0.21125611745513867,
        0.2964989059080963
      ]
    },
    {
      "object": "9",
      "confidence": "0.9311451",
      "detections": [
        0.8058727569331158,
        0.4458424507658643,
        0.2137030995106036,
        0.2986870897155361
      ]
    },
    {
      "object": "2",
      "confidence": "0.9093182",
      "detections": [
        0.3923327895595432,
        0.45842450765864334,
        0.2495921696574225,
        0.3347921225382932
      ]
    },
    {
      "object": "2",
      "confidence": "0.8830928",
      "detections": [
        0.2777324632952692,
        0.44529540481400437,
        0.20799347471451876,
        0.29978118161925604
      ]
    }
  ]
}

#Recopilo las coordenadas X de cada objeto en una lista.

x_coord=[]
for key in dicc:
    if key == "data":
        for entry_data in dicc["data"]:
            i=0
            for key_data in entry_data:
                if key_data == "detections":
                    for value_det in entry_data["detections"]:
                        if i==0:
                            x_coord.append(value_det)
                            i=i+1

#Ordeno la lista.

x_coord.sort()

#Printeo los objetos de cada diccionario en orden de izquiera a derecha en el eje X.

for x in x_coord:
    for key in dicc:
        if key == "data":
            for entry_data in dicc["data"]:
                for key_data in entry_data:
                    if key_data == "detections":
                        for value_det in entry_data["detections"]:
                            if value_det == x:
                                print(f"Objeto: {entry_data['object']}, Coordenada X: {x}")

