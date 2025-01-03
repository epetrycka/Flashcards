package com.flashcards.SocialService.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.BAD_REQUEST)
public class FriendshipAlreadyExistException extends RuntimeException{

    public FriendshipAlreadyExistException(String message) {
        super(message);
    }
}
