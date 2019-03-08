grammar Source;

expr: expr op=('+'|'-'|'&'|'|') expr 
| '(' expr ')'
| ID
;

ID: [a-zA-Z_]+ ;
