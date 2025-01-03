package com.flashcards.SocialService.entity;

import jakarta.persistence.Embeddable;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.io.Serializable;

@Embeddable
@Getter @Setter @ToString
public class FriendshipId implements Serializable {
    private Long userId;
    private Long friendId;
}
