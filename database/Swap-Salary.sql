-- 这里用到了条件逻辑，通过case表达式使用条件逻辑来决定如何执行SQL语句。有两种写法，一种是查找型case表达式，一种是简单型case表达式，分别如下

-- 查找型case表达式

UPDATE salary SET sex = 
    CASE
        WHEN sex = 'f' THEN 'm'
        ELSE 'f'
    END

-- 简单型case表达式

UPDATE salary SET sex = 
    CASE sex
        WHEN 'f' THEN 'm'
        ELSE 'f'
    END