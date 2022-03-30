#!/usr/bin/env python3
import telebot
import tic_tac_toe

bot = telebot.TeleBot("5080725090:AAE-KzWzbXy8-32cnU56UgD6ZWmgvSIuOJY") 

@bot.message_handler(content_types=['text'])
def game(pm):
    tic_tac_toe.game_matrix = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    bot.send_message(pm.chat.id, tic_tac_toe.get_game_matrix_str())
    next_point(pm)


def next_point(pm):
    sent_msg = bot.send_message(pm.chat.id, tic_tac_toe.print_point())
    bot.register_next_step_handler(sent_msg, name_handler)
    
    
def name_handler(pm):
    position = pm.text
    position = position.replace(' ', '')
    if position.isdigit() and len(position) == 2:
        x, y = int(position[0]), int(position[1])
        if (x > 2 or x < 0) or (y > 2 or y < 0):
            bot.send_message(pm.chat.id, 'Шо за координати страні, введи шось інше')
            next_point(pm)
        elif tic_tac_toe.game_matrix[x][y] == tic_tac_toe.first_player or tic_tac_toe.game_matrix[x][y] == tic_tac_toe.second_player:
             bot.send_message(pm.chat.id, 'Ця точка занята')
             next_point(pm)     
        else:
            tic_tac_toe.change_field(x, y) 
            bot.send_message(pm.chat.id, tic_tac_toe.get_game_matrix_str())
            main_audit(pm)
    else:
        bot.send_message(pm.chat.id, 'Шо за координати страні, введи шось інше')
        next_point(pm)



def main_audit(pm):
    tic_tac_toe.main_game()
    if tic_tac_toe.flag == False:
        if tic_tac_toe.audit_field() == False:
            end_game(pm)
        else:
            bot.send_message(pm.chat.id, tic_tac_toe.win(tic_tac_toe.current_player))
            end_game(pm)
    else:
        next_point(pm)
        tic_tac_toe.change_player()

def end_game(pm):
    bot.send_message(pm.chat.id, 'Гра завершена')
    tic_tac_toe.flag = True

bot.polling()







  
