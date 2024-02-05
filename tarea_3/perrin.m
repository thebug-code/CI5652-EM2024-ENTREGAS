% Calcula el n-enésimo Número de Perrin
function r = perrin(n)
    m = [0 1 1; 1 0 0; 0 1 0]; % Metriz inicial
    base = [2; 0; 3];          % Vector inicial
    %result = m^(n-2);
    result = mathpower(m, n - 2);
    temp = result * base;
    r = temp(1,1);


% Eleva una matriz a la n-ésima potencia
function r = mathpower(M, n)
    if n == 1
        r = M;
    else
        P = mathpower(M, floor(n/2));
        if mod(n, 2) == 0
            r = P * P;
        else
            r = P * P * M;
        end
    end
