SELECT 
    f.ID_Func,
    f.Nome_Func,
    c.Nome_CAR_Cargo AS Cargo,
    d.Nome_DEP_Depto AS Departamento,
    f.Data_Contrat,
    f.Data_Demis,
    f.Salario
FROM FUNCIONARIOS f
INNER JOIN CARGOS c 
    ON f.Id_FUN_Cargo = c.Id_CAR_Cargo
INNER JOIN DEPARTAMENTOS d 
    ON f.Id_FUN_Depto = d.Id_DEP_Depto;