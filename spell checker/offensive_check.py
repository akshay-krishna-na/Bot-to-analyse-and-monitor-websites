from profanity_check import predict, predict_prob #need to install profanity_check using pip3
i=predict(["cock"])
if i==1 :
    print("Offensive word found ! ")
else:
    print("Fine")