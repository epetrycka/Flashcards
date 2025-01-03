package com.flashcards.SocialService.mapper;

import com.flashcards.SocialService.dto.UserDto;
import com.flashcards.SocialService.entity.UserEntity;

public class UserMapper {

    public static UserDto mapToUserDto(UserEntity userEntity, UserDto userDto) {
        userDto.setId(userEntity.getId());
        userDto.setUsername(userEntity.getUsername());
        userDto.setEmail(userEntity.getEmail());
        // userDto.setFriendships(userEntity.getFriendships());
        return userDto;
    }

    public static UserEntity mapToUserEntity(UserDto userDto, UserEntity userEntity) {
        userEntity.setUsername(userDto.getUsername());
        userEntity.setEmail(userDto.getEmail());
        // userEntity.setFriendships(userDto.getFriendships());
        return userEntity;
    }
}
