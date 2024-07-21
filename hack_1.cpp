#include <iostream>
#include "libGameLogic.h"
#include <dlfcn.h>
#include <iostream>
#include "libGameLogic.h"
using namespace std;

#include <dlfcn.h>
#include <set>
#include <map>
#include <functional>
#include <string>
#include <vector>
#include<iostream>
#include "libGameLogic.h"

void Player::SetJumpState(bool b){
    printf("[*] SetJumpState(%d)\n",b);
}

void World::Tick(float f)
{
    #void* world = (dlsym(RTLD_NEXT, "GameWorld"));
    #printf("World %p\n",world);
    ClientWorld* world = *((ClientWorld**)(dlsym(RTLD_NEXT, "GameWorld")));
    IPlayer* iplayer = world->m_activePlayer.m_object;
    Player* player = ((Player*)(iplayer));
    Actor* actor = ((Actor*)(iplayer));
    player->m_walkingSpeed = 99999;
    player->m_jumpSpeed = 999;
    player->m_jumpHoldTime = 99999;
}

int main()
{
	std::cout << "Header is Ready!";
	return 0;
}

