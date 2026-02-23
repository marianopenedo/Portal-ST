SELECT 
    d.Nome_DEP_Depto AS Departamento,
    COUNT(f.ID_Func) AS Quantidade_Funcionarios
FROM DEPARTAMENTOS d
LEFT JOIN FUNCIONARIOS f 
    ON f.Id_FUN_Depto = d.Id_DEP_Depto
GROUP BY d.Nome_DEP_Depto
ORDER BY d.Nome_DEP_Depto;