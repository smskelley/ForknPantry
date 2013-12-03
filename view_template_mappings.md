View -> Template Mappings
=========================

|View        |Template        |Dictionary Passed to Template (? denotes optional)
|------------|----------------|------------------------------------------------------------------------------
|Login       |login.html      |{ email? : string } (If supplied, assume email/password was wrong)
|Register    |register.html   |{ email? : string } (If supplied, assume email was taken)
|Pantry      |pantry.html     |{ ingredients : list( {id: int, ingredient: string, user_has: bool} ) }
|Recipes     |recipes.html    |{ recipes : list( {id: int, name: string, link:string, photo_exists: bool} ) }
