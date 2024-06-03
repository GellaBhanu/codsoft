def calc(expr):
    def parse_expr(pos):
        def parse_term(pos):
            result, pos = parse_factor(pos)
            while pos < len(expr) and expr[pos] in '*/':
                op = expr[pos]
                pos += 1
                next_result, pos = parse_factor(pos)
                result = result * next_result if op == '*' else result / next_result
            return result, pos

        def parse_factor(pos):
            if expr[pos] == '(':
                result, pos = parse_expr(pos + 1)
                return result, pos + 1
            else:
                num = ''
                while pos < len(expr) and (expr[pos].isdigit() or expr[pos] == '.'):
                    num += expr[pos]
                    pos += 1
                return float(num), pos

        result, pos = parse_term(pos)
        while pos < len(expr) and expr[pos] in '+-':
            op = expr[pos]
            pos += 1
            next_result, pos = parse_term(pos)
            result = result + next_result if op == '+' else result - next_result
        return result, pos

    expr = expr.replace(' ', '')
    result, _ = parse_expr(0)
    return result
