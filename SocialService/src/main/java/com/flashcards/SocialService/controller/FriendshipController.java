package com.flashcards.SocialService.controller;

import com.flashcards.SocialService.dto.FriendDto;
import com.flashcards.SocialService.entity.FriendshipEntity;
import com.flashcards.SocialService.service.FriendshipService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/friendship")
public class FriendshipController {

    private final FriendshipService friendshipService;

    @Autowired
    public FriendshipController(FriendshipService friendshipService) {
        this.friendshipService = friendshipService;
    }

    @PostMapping
    public ResponseEntity<FriendshipEntity> createFriendship(@RequestBody FriendDto friendDto) {
        try {
            FriendshipEntity friendship = friendshipService.createFriendship(friendDto);
            return new ResponseEntity<>(friendship, HttpStatus.CREATED);
        } catch (RuntimeException e) {
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping("/{userId}/{friendId}")
    public ResponseEntity<FriendshipEntity> getFriendship(@PathVariable Long userId, @PathVariable Long friendId) {
        Optional<FriendshipEntity> friendship = friendshipService.getFriendship(userId, friendId);
        return friendship.map(ResponseEntity::ok)
                .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }

    @GetMapping("/user/{userId}")
    public ResponseEntity<List<FriendshipEntity>> getUserFriends(@PathVariable Long userId) {
        List<FriendshipEntity> friendships = friendshipService.getUserFriends(userId);
        return friendships.isEmpty() ? new ResponseEntity<>(HttpStatus.NO_CONTENT) : new ResponseEntity<>(friendships, HttpStatus.OK);
    }

    @GetMapping("/status/{status}")
    public ResponseEntity<List<FriendshipEntity>> getFriendshipsByStatus(@PathVariable String status) {
        List<FriendshipEntity> friendships = friendshipService.getFriendshipsByStatus(status);
        return friendships.isEmpty() ? new ResponseEntity<>(HttpStatus.NO_CONTENT) : new ResponseEntity<>(friendships, HttpStatus.OK);
    }

    @PutMapping("/{userId}/{friendId}/status")
    public ResponseEntity<FriendshipEntity> updateFriendshipStatus(@PathVariable Long userId, @PathVariable Long friendId, @RequestParam String status) {
        try {
            FriendshipEntity updatedFriendship = friendshipService.updateFriendshipStatus(userId, friendId, status);
            return new ResponseEntity<>(updatedFriendship, HttpStatus.OK);
        } catch (RuntimeException e) {
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @DeleteMapping("/{userId}/{friendId}")
    public ResponseEntity<Void> deleteFriendship(@PathVariable Long userId, @PathVariable Long friendId) {
        try {
            friendshipService.deleteFriendship(userId, friendId);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (RuntimeException e) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
