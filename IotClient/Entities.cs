using System;
using System.Text.Json;

namespace IotClient{

class Client{

    public static Dictionary<string, double> readJson(string filepath){

        if(!File.Exists(filepath)){
            throw new Exception("Il file non esiste");
        }

        string jsonContent = File.ReadAllText(filepath);
        var simulationData = JsonSerializer.Deserialize<Dictionary<string, JsonElement>>(jsonContent);

        if (simulationData == null){
            throw new Exception("Json non valido");
        }

        // TODO MODIFICARE QUESTI VALORI
        double valore1 = simulationData["valore1"].GetDouble();
        double valore2 = simulationData["valore2"].GetDouble();
        double valore3 = simulationData["valore3"].GetDouble();

        Dictionary<string, double> elementi = new Dictionary<string, double>();
        elementi.Add("Valore 1", valore1);
        elementi.Add("Valore 2", valore2);
        elementi.Add("Valore 3", valore3);
        // ----------------------------


        return elementi;

    }
}
}