ohml_trusted <- read.csv("C:/Users/Gisele/Downloads/ohml_trusted.csv", header=FALSE, skip = 1)
#corrigir esse arquivo com o caminho do de vcs!

summary(ohml_trusted[6]) #pegando a coluna que capta de todos os cores
print(ohml_trusted[6])

n = 200 #definindo tamanho da amostra

temp_total <- ohml_trusted[6]
sd(temp_total$V6) #definindo o desvio padrão

#simulação feita apartir de uma distribuição
temperatura <- abs(round(rnorm(n,71,7.21),2))

#plotando o grafico
hist(temperatura,
     main = "Variação de temperatura",
     ylab = "Frequência",
     xlab = "Temperatura")

