# SlothBot

A simple bot that identifies information from
users and stores somewhere.

## Simple chat

This bot has been created for a specific use,
each branch consists of different
behaviours. An example is `bot/pet-lover`
that understands the following dialog:

```shell
>> Oi
> Olá, qual o seu nome?
>> Meu nome é fulano.
> Prazer, fulano, eu sou o SlothBot. Você
tem algum animal de estimação? Se sim, qual
o nome e a idade dele?
>> Eu tenho um gato chamado Gato e ele tem
122 anos.
> O que eu entendi é que você tem um gato
chamado Gato e ele tem 122 anos de idade.
É isso mesmo?
>> Sim.
> Que bom, meu serviço está feito!
>> Ok
```

The bot has to understand the person's name
and identify if a person has a pet, if the
person does have it, the bot must register
the pet's kind, name and age.
After that, he must check with the user if
the information is correct. If yes, then
the bot has done it's purpose, otherwise
it must request the user to repeat the
information.

## Bots

Currently implemented bots are

- None
