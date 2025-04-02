def customStrip(text):
    return (text[4:] if text[:4] == "    " else text)

def arithmetic_arranger(problems, show_answers=False):
    
    problem = []
    lengthDiff = []
    txt = ''
    txt1 = ''
    txt2 = ''
    txt3 = ''
    txt4 = ''

    for i in problems:
        problem.append(i.split(' '))
        if (len(problem)) > 5: return 'Error: Too many problems.'

    for i in problem[::-1]:
        lengthDiff.append(len(i[0]) - len(i[2]))

        if not i[0].isdigit() or not i[2].isdigit():
            return 'Error: Numbers must only contain digits.'

        if (len(i[0]) > 4) or (len(i[2]) > 4):
            return 'Error: Numbers cannot be more than four digits.'

        if lengthDiff[len(lengthDiff)-1] >= 0: 
            txt1 = ' ' * 6 + i[0] + txt1
            txt2 = ' ' * 4 + i[1] + ' ' * (lengthDiff[len(lengthDiff)-1] + 1) + i[2] + txt2
            txt3 = ' ' * 4 + '-' * (len(i[0])+2) + txt3
            
            if i[1] == '+':
                txt4 = ' ' * (4 + len(i[0]) + 2 - len(str(int(i[0]) + int(i[2])))) + str(int(i[0]) + int(i[2])) + txt4
            elif i[1] == '-':
                txt4 = ' ' * (4 + len(i[0]) + 2 - len(str(int(i[0]) - int(i[2])))) + str(int(i[0]) - int(i[2])) + txt4 
            else: return "Error: Operator must be '+' or '-'." 
        
        else: 
            txt1 = ' ' * (4+2+abs(lengthDiff[len(lengthDiff)-1])) + i[0] + txt1
            txt2 = ' ' * 4 + i[1] + ' ' + i[2] + txt2 
            txt3 = ' ' * 4 + '-' * (len(i[2])+2) + txt3

            if i[1] == '+':
                txt4 = ' ' * (4 + len(i[2]) + 2 - len(str(int(i[0]) + int(i[2])))) + str(int(i[0]) + int(i[2])) + txt4
            elif i[1] == '-':
                txt4 = ' ' * (4 + len(i[2]) + 2 - len(str(int(i[0]) - int(i[2])))) + str(int(i[0]) - int(i[2])) + txt4
            else: return "Error: Operator must be '+' or '-'."
            
    txt = f'{customStrip(txt1)}\n{customStrip(txt2)}\n{customStrip(txt3)}\n{customStrip(txt4)}' if show_answers else f'{customStrip(txt1)}\n{customStrip(txt2)}\n{customStrip(txt3)}'
    return txt
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "3 + 495"])}')
