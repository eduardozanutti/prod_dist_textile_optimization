### Sets

- $S$: conjunto de SKUs (unidades de estoque, como tamanhos de um material)  
- $F$: conjunto de famílias de produto  
- $G$: conjunto de grupos de gerência  
- $C$: conjunto de centros de distribuição (CDs) 
- $T$: conjunto de períodos de tempo (semanas)  
- $S_f[f]$: conjunto de SKUs pertencentes à família $f$


### Parameters

- $p_k$: preço unitário de venda do SKU $k$  
- $r_{ijkt}$: custo de transporte do CD origem $i$ para CD destino $j$ para o SKU $k$ no período $t$  
- $d_{ikt}$: demanda do SKU $k$ no CD $i$ no período $t$  
- $I0_{ik}$: estoque inicial do SKU $k$ no CD $i$  
- $\tau_{ij}$: leadtime de transporte do CD $i$ para o CD $j$  
- $s_{it}$: custo fixo de setup de produção por CD e período  
- $c_{ikt}$: custo variável de produção do SKU $k$ no período $t$  
- $h_{ikt}$: custo de armazenagem do SKU $k$ no CD $i$ no período $t$  
- $\alpha$: taxa de desconto (valor presente líquido)  
- $Q_{min}$: quantidade mínima total de produção  
- $Q_{max}$: quantidade máxima total de produção  
- $cap_i$: capacidade de envio do CD $i$ por período


### Variables

- $x_{ikt}$: quantidade produzida do SKU $k$ no CD $i$ no período $t$  
- $w_{ijkt}$: quantidade enviada do SKU $k$ do CD $i$ para o CD $j$ no período $t$  
- $y_{ikt}$: variável binária de ativação da produção do SKU $k$ no CD $i$ no período $t$  
- $z_{ift}$: variável binária de ativação do setup do produto/família $f$ no CD $i$ no período $t$  
- $z_{ijkt}$: variável binária de ativação do transporte do SKU $k$ do CD $i$ para o CD $j$ no período $t$  
- $v_{ikt}$: quantidade vendida do SKU $k$ no CD $i$ no período $t$  
- $I_{ikt}$: estoque do SKU $k$ no CD $i$ no período $t$


### Constraints

1. **Atendimento da Demanda**  
$
v_{ikt} \le d_{ikt}
$
garante que as vendas não excedam a demanda prevista.


2. **Balanceamento de Estoque**    
$
I_{ikt-1} + x_{ikt} + \sum_{j \neq i} w_{jikt - \tau_{ji}} - \sum_{j \neq i} w_{ijkt} - I_{ikt} = v_{ikt}
$
para os períodos posteriores,  
e  
$
I0_{ik} + x_{ikt} - \sum_{j \neq i} w_{ijkt} - I_{ikt} = v_{ikt}
$
no primeiro período.


3. **Proibição de envio a partir do CD 1**  
$
w_{1jkt} = 0 \quad \forall j \neq 1
$


4. **Ativação Big-M da Produção**  
$
x_{2kt} \le M \cdot y_{2kt}
$
garante coerência da produção com ativação binária.


5. **Capacidade de Envio**  
$
\sum_{j \neq i} \sum_{k} w_{ijkt} \le cap_i
\quad \forall i \neq 1
$


6. **Mínimo de envio por gerência (comentado opcional)**  
se quiser ativar:  
$
w_{ijkt} \ge g\_min_{ig} \cdot z_{ijkt}
$
mas precisa complementar com Big-M superior para garantir coerência binária.


7. **Ativação da Família (setup)**  
$
z_{ift} \ge y_{ikt} \quad \forall k \in S_f[f]
$
assegura ativação de setup ao produzir qualquer SKU de um produto.


8. **Integrality**  
todas as variáveis de venda, estoque e transporte são não-negativas,  
as binárias indicam ativação de produção e transporte.


### Função Objetivo

minimizar o custo total do sistema:
$$
\begin{aligned}
\min \Bigg\{
& \sum_{ikt} c_{ikt} x_{ikt}
+ \sum_{ift} s_{it} z_{ift}
+ \sum_{ikt} h_{ikt} I_{ikt}
+ \sum_{ijkt} r_{ijkt} w_{ijkt} \\
& + \sum_{ikt} (d_{ikt} - v_{ikt}) \, p_k \, \alpha^{(t-1)}
\Bigg\}
\end{aligned}
$$


### Função Objetivo

$$
\min \left\{
\sum_{i,k,t} c_{ikt} x_{ikt}
+ \sum_{i,f,t} s_{it} z_{ift}
+ \sum_{i,k,t} h_{ikt} I_{ikt}
+ \sum_{i,j,k,t} r_{ijkt} w_{ijkt}
+ \sum_{i,k,t} (d_{ikt} - v_{ikt}) \, p_{k} \, \alpha^{(t-1)}
\right\}
$$

### Restrições

#### Atendimento da demanda

$$
v_{ikt} \leq d_{ikt} \tag{1}
$$

#### Balanceamento de Estoque

Para $t > 1 $:

- CD Fábrica ( $ i = 2 $ ):
$$
I_{ikt-1} + x_{ikt}
+ \sum_{j \neq i} w_{jikt - \tau_{ji}}
- \sum_{j \neq i} w_{ijkt}
- I_{ikt}
= v_{ikt}
$$

- Demais CDs:
$$
I_{ikt-1}
+ \sum_{j \neq i} w_{jikt - \tau_{ji}}
- \sum_{j \neq i} w_{ijkt}
- I_{ikt}
= v_{ikt}
$$

Para $ t=1 $:

- CD Fábrica:
$$
I0_{ik} + x_{ikt}
- \sum_{j \neq i} w_{ijkt}
- I_{ikt}
= v_{ikt}
$$

- Demais CDs:
$$
I0_{ik}
- \sum_{j \neq i} w_{ijkt}
- I_{ikt}
= v_{ikt}
\tag{2}
$$


#### Big M Produção

$$
x_{2kt} \leq M \cdot y_{2kt}
\tag{3}
$$


#### Ativação da Família

$$
z_{2ft} \geq y_{2kt}
\quad \forall k \in S_f[p]
\tag{4}
$$


#### (5) Pedido Mínimo

$$
\sum_{k} x_{2kt} \geq Q_{min}
\tag{5}
$$


#### Pedido Máximo

$$
\sum_{k} x_{2kt} \leq Q_{max}
\tag{6}
$$


#### Proibição de Produção em CDs 1 e 3

$$
\sum_{k} x_{ikt} = 0
\quad \forall i \neq 2
\tag{7}
$$


#### (8) Envio proibido de CD 1

$$
w_{1jkt} = 0
\quad \forall j \neq 1
\tag{8}
$$


#### (9) Capacidade de Envio

$$
\sum_{j \neq i} \sum_{k} w_{ijkt} \leq cap_{i}
\quad \forall i \neq 1
\tag{9}
$$



