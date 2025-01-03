package com.flashcards.SocialService.repository;

import com.flashcards.SocialService.entity.FriendshipEntity;
import com.flashcards.SocialService.entity.FriendshipId;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface FriendshipRepository extends JpaRepository<FriendshipEntity, FriendshipId> {

    Optional<FriendshipEntity> findByUser_IdAndFriend_Id(Long userId, Long friendId);

    List<FriendshipEntity> findByUser_Id(Long userId);

    List<FriendshipEntity> findByStatus(String status);

    Optional<FriendshipEntity> findByUser_IdAndFriend_IdAndStatus(Long userId, Long friendId, String status);
}
