package com.flashcards.SocialService.mapper;

import com.flashcards.SocialService.dto.FriendDto;
import com.flashcards.SocialService.entity.FriendshipEntity;
import com.flashcards.SocialService.entity.UserEntity;
import com.flashcards.SocialService.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class FriendshipMapper {

    private final UserRepository userRepository;

    @Autowired
    public FriendshipMapper(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public FriendDto mapToFriendDto(FriendshipEntity friendshipEntity, FriendDto friendDto) {
        friendDto.setSenderNickname(friendshipEntity.getUser().getUsername());
        friendDto.setRecipientNickname(friendshipEntity.getFriend().getUsername());
        friendDto.setStatus(friendshipEntity.getStatus());
        return friendDto;
    }

    public FriendshipEntity mapToFriendshipEntity(FriendDto friendDto, FriendshipEntity friendshipEntity) {
        UserEntity user = userRepository.findByUsername(friendDto.getSenderNickname())
                .orElseThrow(() -> new RuntimeException("User not found with nickname: " + friendDto.getSenderNickname()));

        UserEntity friend = userRepository.findByUsername(friendDto.getRecipientNickname())
                .orElseThrow(() -> new RuntimeException("Friend not found with nickname: " + friendDto.getRecipientNickname()));

        friendshipEntity.setUser(user);
        friendshipEntity.setFriend(friend);
        friendshipEntity.setStatus(friendDto.getStatus().toString());
        return friendshipEntity;
    }
}
