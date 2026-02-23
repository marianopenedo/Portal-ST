SELECT 
    f.Nome_Func,
    f.Salario,
    c.Nome_CAR_Cargo,
    d.Nome_DEP_Depto
FROM FUNCIONARIOS f
INNER JOIN CARGOS c 
    ON f.Id_FUN_Cargo = c.Id_CAR_Cargo
INNER JOIN DEPARTAMENTOS d 
    ON f.Id_FUN_Depto = d.Id_DEP_Depto
WHERE f.Salario > 2900;