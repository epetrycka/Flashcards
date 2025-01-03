package com.flashcards.SocialService.service;

import com.flashcards.SocialService.entity.FriendshipEntity;
import com.flashcards.SocialService.dto.FriendDto;

import java.util.List;
import java.util.Optional;

public interface FriendshipService {

    FriendshipEntity createFriendship(FriendDto friendDto);

    Optional<FriendshipEntity> getFriendship(Long userId, Long friendId);

    List<FriendshipEntity> getUserFriends(Long userId);

    List<FriendshipEntity> getFriendshipsByStatus(String status);

    FriendshipEntity updateFriendshipStatus(Long userId, Long friendId, String status);

    void deleteFriendship(Long userId, Long friendId);
}
