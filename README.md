# AIC_5101C_BERTRAND_IM-SAROEUN_JUREK

Ce projet implémente un bot Discord qui verifie que les sujets de différents channels de discussions sont bien respectés.

La version actuelle utilise un modèle de LLM qui catégorise les messages en deux catégories : Sport ou Technologie.
Afin d'utiliser ce bot, il faut:
- un serveur Discord
- avec deux channels "sport" et "technologies"

Il vous faudra également alimenter vous-même le projet avec un fichier .env contenant l'objet DISCORD_TOKEN, token de votre bot.