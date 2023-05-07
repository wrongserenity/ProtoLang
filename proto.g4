grammar proto;
program       :
              declaration*
              statement*
              ;

// Parse rule for variable declarations

declaration     : VAL ID SEMICOLON                                              #valDecl
                | FUNC ID paramdecl funcbody funcreturn? ENDFUNC     #funcDecl
                ;

paramdecl : LPAREN ID? (COMMA ID)* RPAREN;

funcbody : statement*;

funcreturn : RETURN expr SEMICOLON;

// Parse rule for statements

statement   : ifstmt
            | whilestmt
            | printstmt
            | assignstmt
            | term
            | savelinesstmt
            | readfilestmt
            ;

// statement rules

ifstmt      :
            IF condblock
            (ELSE IF condblock)*
            (ELSE statement*)?
            ENDIF
            ;



whilestmt   :
            WHILE LPAREN expr RPAREN
            statement*
            ENDWHILE
            ;

printstmt      :
               PRINT expr SEMICOLON
               ;

assignstmt      :
                ID ASSIGN expr SEMICOLON
                ;

savelinesstmt   :
                SAVELINES term SEMICOLON
                ;

readfilestmt    :
                READFILE term SEMICOLON
                ;

condblock   : LPAREN expr RPAREN
            statement*
            ;

// Parse rule for expressions

expr    : MINUS expr                           #unaryMinusExpr
        | NOT expr                             #notExpr
        | expr op=(MULT | DIV | MOD) expr      #multiplicationExpr
        | expr op=(PLUS | MINUS) expr          #additiveExpr
        | expr op=(LTEQ | GTEQ | LT | GT) expr #relationalExpr
        | expr op=(EQ | NEQ) expr              #equalityExpr
        | expr AND expr                        #andExpr
        | expr OR expr                         #orExpr
        | term                                 #termExpr
        ;

// Parse rule for terms

term    : LPAREN expr RPAREN    #parenAtom
        | INTEGER               #integerAtom
        | FLOAT                 #floatAtom
        | (TRUE | FALSE)        #booleanAtom
        | ID                    #idAtom
        | funccall              #funcAtom
        | STRING                #stringAtom
        ;

funccall : ID parampass;

parampass :     LPAREN expr (COMMA expr)* RPAREN;

// Reserved Keywords
////////////////////////////////

IF: 'if';
ELSE : 'else';
ENDIF: 'endif';
WHILE: 'while';
ENDWHILE: 'endwhile';
PRINT: 'print';

VAL: 'val';
FUNC: 'func';
RETURN: 'return';
ENDFUNC: 'endfunc';

SAVELINES : 'savelines';
READFILE : 'readfile';

// Operators
OR : '||';
AND : '&&';
EQ : '==';
NEQ : '!=';
GT : '>';
LT : '<';
GTEQ : '>=';
LTEQ : '<=';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';
MOD : '%';
NOT : '!';

// Semicolon and parentheses
SEMICOLON: ';';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
ASSIGN: '=';

// Values

NIL : 'nil';

TRUE : 'true';
FALSE : 'false';

INTEGER: [0-9]+;

FLOAT   : [0-9]+ '.' [0-9]*
        | '.' [0-9]+
        ;

STRING
 : '"' (~["\r\n] | '""')* '"'
 ;

// Variable id
ID: [a-z]+;

// Ignore all white spaces
WS: [ \t\r\n]+ -> skip ;