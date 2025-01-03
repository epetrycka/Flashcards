package com.flashcards.SocialService.service.impl;

import com.flashcards.SocialService.entity.FriendshipEntity;
import com.flashcards.SocialService.dto.FriendDto;
import com.flashcards.SocialService.repository.FriendshipRepository;
import com.flashcards.SocialService.repository.UserRepository;
import com.flashcards.SocialService.service.FriendshipService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class FriendshipServiceImpl implements FriendshipService {

    private final FriendshipRepository friendshipRepository;
    private final UserRepository userRepository;

    @Autowired
    public FriendshipServiceImpl(FriendshipRepository friendshipRepository, UserRepository userRepository) {
        this.friendshipRepository = friendshipRepository;
        this.userRepository = userRepository;
    }

    @Override
    public FriendshipEntity createFriendship(FriendDto friendDto) {
        var user = userRepository.findByUsername(friendDto.getSenderNickname())
                .orElseThrow(() -> new RuntimeException("User not found with nickname: " + friendDto.getSenderNickname()));

        var friend = userRepository.findByUsername(friendDto.getRecipientNickname())
                .orElseThrow(() -> new RuntimeException("Friend not found with nickname: " + friendDto.getRecipientNickname()));

        FriendshipEntity friendship = new FriendshipEntity();
        friendship.setUser(user);
        friendship.setFriend(friend);
        friendship.setStatus(friendDto.getStatus().toString());

        return friendshipRepository.save(friendship);
    }

    @Override
    public Optional<FriendshipEntity> getFriendship(Long userId, Long friendId) {
        return friendshipRepository.findByUser_IdAndFriend_Id(userId, friendId);
    }

    @Override
    public List<FriendshipEntity> getUserFriends(Long userId) {
        return friendshipRepository.findByUser_Id(userId);
    }

    @Override
    public List<FriendshipEntity> getFriendshipsByStatus(String status) {
        return friendshipRepository.findByStatus(status);
    }

    @Override
    public FriendshipEntity updateFriendshipStatus(Long userId, Long friendId, String status) {
        FriendshipEntity friendship = friendshipRepository.findByUser_IdAndFriend_Id(userId, friendId)
                .orElseThrow(() -> new RuntimeException("Friendship not found"));

        friendship.setStatus(status);

        return friendshipRepository.save(friendship);
    }

    @Override
    public void deleteFriendship(Long userId, Long friendId) {
        FriendshipEntity friendship = friendshipRepository.findByUser_IdAndFriend_Id(userId, friendId)
                .orElseThrow(() -> new RuntimeException("Friendship not found"));

        friendshipRepository.delete(friendship);
    }
}
