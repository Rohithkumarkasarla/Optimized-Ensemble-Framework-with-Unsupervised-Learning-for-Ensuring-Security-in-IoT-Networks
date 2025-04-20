from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd

classifier = joblib.load('DecisionTree_weights.pkl')

'''def form(request):
    if request.method=='POST':
        #nnamed = request.POST.get('unnamed')
        id_orig_p = request.POST.get('id_orig_p')
        id_resp_p = request.POST.get('id_resp_p')
        proto = request.POST.get('proto')
        service = request.POST.get('service')
        flow_duration = request.POST.get('flow_duration')
        fwd_pkts_tot = request.POST.get('fwd_pkts_tot')
        bwd_pkts_tot = request.POST.get('bwd_pkts_tot')
        fwd_data_pkts_tot = request.POST.get('fwd_data_pkts_tot')
        bwd_data_pkts_tot = request.POST.get('bwd_data_pkts_tot')
        features = [[
            float(id_orig_p) if id_orig_p is not None else 0.0,
            float(id_resp_p) if id_resp_p is not None else 0.0,
            float(proto) if proto is not None else 0.0,
            float(service) if service is not None else 0.0,
            float(flow_duration) if flow_duration is not None else 0.0,
            float(fwd_pkts_tot) if fwd_pkts_tot is not None else 0.0,
            float(bwd_pkts_tot) if bwd_pkts_tot is not None else 0.0,
            float(fwd_data_pkts_tot) if fwd_data_pkts_tot is not None else 0.0,
            float(bwd_data_pkts_tot) if bwd_data_pkts_tot is not None else 0.0
            ]]
        #test = pd.read_csv((r"test.csv")
        predict = classifier.predict(features)
        return render(request,form.html,predict)
    return render(request,'form.html')'''

def form(request):
    if request.method == 'POST' and request.FILES['predict']:
        csv=request.FILES['predict']
        data=pd.read_csv(csv)
        Labels = ['proto','service']
        for i in Labels:
            data[i] = LabelEncoder().fit_transform(data[i])
        data
        predict = classifier.predict(data)
        return render (request,'Form_predict.html',{'predicts':predict})
    return render (request,'Form_predict.html')
# Create your views here.
