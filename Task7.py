#Equation solver

def main():

    input = '- x = - 1'
    #Need to collect all non-algebraic terms on one side

    def equation_solver(equation):
        [lhs, rhs] = equation.split("=")
        
        if "x" not in lhs:
            rhs_no_x = rhs.replace("x", '')

            if len(rhs_no_x) > 1:
                #Checking for inverse variable
                try:
                    rhs_value = eval(rhs_no_x)
                except:
                    solved_lhs = eval(lhs)
                    answer = solved_lhs
                    return answer

                #Moving values across and inverting them
                solved_lhs = eval(lhs)
                solved_lhs += (-rhs_value)
                answer = solved_lhs
                return answer

            #Simply evaluating one side in easy case
            answer = eval(lhs)
            return answer

        else:
            lhs_no_x = lhs.replace("x", '')

            if len(lhs_no_x) > 1:
                try:
                    lhs_value = eval(lhs_no_x)
                except:
                    solved_rhs = eval(rhs)
                    answer = solved_rhs
                    return answer

                solved_rhs = eval(rhs)
                solved_rhs += (-lhs_value)
                answer = solved_rhs
                return answer

            answer = eval(lhs)
            return answer


    print(equation_solver(input))


if __name__ == "__main__":
    main()