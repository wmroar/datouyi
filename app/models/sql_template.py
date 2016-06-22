# -*- coding : utf-8 -*-

KIND_TPL = {
    'recure_tpl' : """WITH  RECURSIVE cte as (
        SELECT id,pid,name,des,1 AS level from datouyi.kind where pid is null
        UNION ALL
        SELECT t.id,t.pid,t.name,t.des, c.level + 1
        from cte c
        JOIN datouyi.kind t
        on c.id = t.pid
        )
        SELECT * from cte where 2 > 1 %(condition)s
        ORDER BY  level;
    """
}