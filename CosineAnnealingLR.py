model = nn.Linear(10, 2)
optimizer = optim.SGD(model.parameters(), lr=1.)
steps = 10
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, steps)

for epoch in range(5):
    for idx in range(steps):
        scheduler.step()
        print(scheduler.get_lr())
    
    print('Reset scheduler')
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, steps)
    
>> 
[0.9516553824444453]
[0.8386590697412432]
[0.6968044012954536]
[0.5395961100811341]
[0.38196601125010515]
[0.23872875703131577]
[0.12295598939793909]
[0.04424211972088169]
[0.006271407734229157]
[0.0]