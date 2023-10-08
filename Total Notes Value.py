# suming all notes in amount.

notes = [2000,500,200,100,50,20,10,5,2,1]
amount = 0
for am in notes:
    n_notes = int(input(f'No. of {am} Rs notes\t:'))
    amount += n_notes*am

print("Amount Calculated:",amount)
