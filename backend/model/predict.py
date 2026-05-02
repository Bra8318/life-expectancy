import pickle
import pandas as pd

with open ('model/model.pkl','rb') as f:
    models = pickle.load(f)
# print(models.keys())
# print(models['Economic'])
#print(models['Economic']['target'].name) 



def predict_data(model_name:str,user_input:dict):
        input_data = pd.DataFrame([user_input])
        model = models[model_name]['model']
        prediction = model.predict(input_data)
        target = models[model_name]['target']
        stat = models[model_name].get("stat", {})

        def safe(obj):
            if isinstance(obj,pd.DataFrame):
                return obj.to_dict(orient="records")
            if isinstance(obj,pd.Series):
                return obj.to_dict()
            if hasattr(obj,'tolist'):
                return obj.tolist()
            return obj
         
        def format_prediction(prediction,target):
            if isinstance(target,pd.Series):
                target_name = [target.name]
            else:
                target_name = list(target)
            values = prediction.tolist() if hasattr(prediction,'tolist') else prediction

            if isinstance(values,list) and len(values) == 1 and isinstance(values[0],list):
                values = values[0]
            
            values = [float(v) for v in values]
                
            if len(target_name) == 1:
                return {target_name[0]: float(values[0])}
    
            if len(target_name) == len(values):
                return dict(zip(target_name,values))
            return values
        
        group_stat = stat.get("group",{})
        if isinstance(group_stat,dict):
            group_stat = {k:(v.item() if hasattr(v,'item')else v) for k,v in group_stat.items()}
        
        response = {
            "prediction": format_prediction(prediction,target),
            "model" : model_name,
            "world_stat": safe(stat.get("stat",{})),
            "group_stat": safe(stat.get("group",{})),
            "ranking": safe(stat.get("ranking",{})),
            "percentile": safe(stat.get("percentile",{}))
        }
        return response

        # if isinstance(target,pd.Series):
        #     target_name = [target.name]
        # else:
        #     target_name = target
        # if hasattr(prediction,'tolist'):
        #     values = prediction.tolist()

        #     if isinstance(values[0],list):
        #         values = values[0]
        #     if len(target_name) == 1:
        #         return {target_name[0]: float(values[0])}
        #     return dict(zip(target, values))
        # return prediction

 

    
