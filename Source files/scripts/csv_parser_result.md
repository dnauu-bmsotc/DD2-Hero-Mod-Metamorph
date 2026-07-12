<details>
<summary>Achievement</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_allTags|Tags|Yes||
|m_anyTags|Tags|Yes||
|m_avoidTags|Tags|Yes||
|m_destinationTags|Tags|No||
|m_eachTags|Tags|Yes||
|m_number|2...4|No||
|m_sourceTags|Tags|No||
|m_targetFloat|0.25...20000.00|No||
|m_targetInt|1...100|No||
|m_type|<details><summary>Click&#8201;to&#8201;expand</summary>actor_death<br>actor_death_combat_sum<br>actor_death_count_from_source<br>actor_death_inventory_full<br>actor_death_run_sum<br>actor_death_skill_use_active_tokens<br>actor_death_with_source<br>affinity_overstress<br>affinity_overstress_chain<br>altar_of_hope_total_progress<br>biome_complete<br>biome_complete_group<br>collected_trophies<br>combat_party_has_quirk<br>combat_skill_hits<br>combat_victory<br>confession_victory<br>confession_victory_consecutive<br>driving_distance<br>game_mode_transition<br>hire_mercenary<br>hospital_full_service<br>inn_treasure_campaign_sum<br>inn_visit_all<br>inventory_full<br>inventory_item_add<br>inventory_item_purchase<br>item_triggered_effects<br>kingdom_campaign_use_items<br>kingdom_inn_capstones<br>kingdom_kill_contracts<br>kingdom_victory<br>kingdom_victory_uninfected_heroes<br>node_deliverable_campaign_sum<br>party_classes<br>party_relationship_pair<br>party_relationships<br>party_wipe<br>profile_unlock<br>profile_unlock_group<br>quest_complete<br>quest_step_story_choices<br>release_anniversary<br>replacement_hero_add<br>roster_confirm<br>roster_relationships_unique<br>run_end<br>skill_health_damage<br>skill_mastery<br>skill_use<br>skill_use_processed_tokens<br>tokens_removed_campaign_sum<br></details>|No||

</details>

<details>
<summary>ActOut</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |Yes||
|any_conditions|Condition&nbsp;ID |No||
|effects|Effect&nbsp;ID |Yes||
|m_ActorType|OTHER<br>PARTY<br>PERFORMER<br>SELF<br>TARGET|No||
|m_AdditionalSkillTags|Tags|No||
|m_BarkSwapPerformerAndTarget|Boolean|No||
|m_Chance|0.02...0.40|No||
|m_DelayCooldownDurationAmount|2...2|No||
|m_DelayCooldownDurationType|every_turn_end|No||
|m_DisplayType|crimson_curse_bloodlust<br>crimson_curse_craving<br>crimson_curse_passive<br>crimson_curse_wasting<br>negative<br>positive|No||
|m_EffectSwapPerformerAndTarget|Boolean|No||
|m_IsFriendly|Boolean|No||
|m_IsGuardingValid|Boolean|No||
|m_IsMultihitValid|Boolean|No||
|m_IsZoomIn|Boolean|No||
|m_Priority|0.25...1.00|No||
|m_RandomStartCooldownDurationAmount|3...3|No||
|m_RandomStartCooldownDurationType|round_end|No||
|m_SelectCooldownDurationAmount|1...3|No||
|m_SelectCooldownDurationType|node<br>round_end|No||
|m_SelectDelayTags|Tags|No||
|m_SourceIdLimit|1...1|No||
|m_SourceTypeLimit|1...2|No||
|m_Tags|Tags|Yes||
|m_Type|banter<br>skill_additional<br>skill_after<br>skill_before<br>start_turn|No||

</details>

<details>
<summary>ActorDataActOut</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|act_outs|ActOut&nbsp;ID |Yes||

</details>

<details>
<summary>ActorDataClass</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ActorChangeClassHealType|MAX_HP_DELTA|No||
|m_ActorControllerType|RANDOM|No|RANDOM makes this actor act on their own. Also supports INPUT value|
|m_ClearContainerKeepTags|Tags|Yes||
|m_ClearContainerTypes|BuffContainer<br>DebuffContainer<br>DotContainer<br>TokenContainer|Yes|If another actor was transformed into this actor, buffs/DOTs/tokens will be removed. This is important, for example, for the final Confession boss that uses hidden tokens to track if a hero is still alive.|
|m_DeathBackActorClassIds|<sub>parse fail</sub>|No||
|m_DeathChainIds|<sub>parse fail</sub>|No|If the actor referenced by this field dies, this actor dies too|
|m_DeathChainLootIds|none|No||
|m_DeathClassAddsTurn|Boolean|No||
|m_DeathClassRemovesTurns|Boolean|No||
|m_DeathFrontActorClassIds|<sub>parse fail</sub>|No||
|m_DeathLootIds|LootTable&nbsp;ID |No||
|m_DeathRound|0...99|No||
|m_DefaultActorDataPathId|ActorDataPath&nbsp;ID |No||
|m_EquippedCombatSkillLimit|5...5|No|It can be increased, but values above 6 lead to UI overlaps, at least on my screen.|
|m_ExpeditionUnlockId|Unlock&nbsp;ID |No||
|m_IgnoredSkillAttributeTypes|BUFF_ADD<br>QUIRK_ADD<br>TOKEN_ADD|Yes|Disallows this actor to gain buffs/quirks/tokens|
|m_IsActOutSkillAdditionalInvalidating|Boolean|No||
|m_IsActoutValid|Boolean|No||
|m_IsBarkTriggerValid|Boolean|No||
|m_IsBattleComplete|Boolean|No|If set to True, then fights will finish even if this actor is alive|
|m_IsCombatHoverable|Boolean|No||
|m_IsDeathPhase|Boolean|No||
|m_IsEffectsReasonValid|Boolean|No||
|m_IsHealthless|Boolean|No||
|m_IsRelationshipValid|Boolean|No||
|m_IsStallCounted|Boolean|No||
|m_IsStallInvalidating|Boolean|No||
|m_IsStartRoundSkillsCounted|Boolean|No||
|m_IsStressTriggerValid|Boolean|No||
|m_IsTargetable|Boolean|No||
|m_IsTickTriggerValid|Boolean|No||
|m_LocalizationGender|female<br>male|No||
|m_NameOverrideId|<sub>parse fail</sub>|No||
|m_QuirkContainerId|QuirkContainer&nbsp;ID |No|A default roster_quirk_container can be swapped to make hero's starting quirks predefined.|
|m_RankTags|Example: `m_RankTags,2,sweet_spot,3,sweet_spot,`<br>Slot 2 values:<br>sweet_spot|Yes||
|m_ReserveActorDataPathId|ActorDataPath&nbsp;ID |No||
|m_ResistAlwaysIds|Resist&nbsp;ID |Yes||
|m_ResistMaxOverrides|Example: `m_ResistMaxOverrides,death,1,`<br>Slot 1 values:<br>death|Yes|Caps specified resistances so they can't go above the given value|
|m_ResistMinOverrides|Example: `m_ResistMinOverrides,death,0.33,`<br>Slot 1 values:<br>death|Yes|Caps specified resistances so they can't go below the given value|
|m_RosterOrderPriority|5...20|No|Specifies hero's order priority at the Crossroads. PD's priority is 19, Abomination's priority is 5.|
|m_Size|1...4|No||
|m_SkillBlockId|SkillBlock&nbsp;ID |No||
|m_SpawnLootIds|LootTable&nbsp;ID |No||
|m_StartingRosterStatusType|hire<br>idle|No||
|m_Tags|Tags|Yes|I guess that brain_blessing means that this actor can become ordained in Act 1. Other blessings: lungs_blessing, eyes_blessing, arms_blessing, final_blessing,|
|m_TokenViewValid|Boolean|No||
|modes|ActorDataMode&nbsp;ID |Yes||
|overstresses|Overstress&nbsp;ID |Yes||
|skill_sets|SkillSet&nbsp;ID |Yes||
|summon_any_conditions|Condition&nbsp;ID |Yes||

</details>

<details>
<summary>ActorDataEffects</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|actor_effect_triggers|ActorEffectTrigger&nbsp;ID |Yes||
|change_class_effects|Effect&nbsp;ID |Yes||
|combat_end_effects|Effect&nbsp;ID |Yes||
|combat_health_damage_apply_limit|1...1|No||
|combat_health_damage_apply_limit_effects|Effect&nbsp;ID |Yes||
|combat_health_damage_effects|Effect&nbsp;ID |Yes||
|combat_health_damage_enemy_team_effects|Effect&nbsp;ID |No||
|combat_health_damage_friendly_team_effects|Effect&nbsp;ID |No||
|combat_health_heal_apply_limit|1...1|No||
|combat_health_heal_apply_limit_effects|Effect&nbsp;ID |Yes||
|combat_health_heal_effects|Effect&nbsp;ID |Yes||
|combat_health_heal_enemy_team_effects|Effect&nbsp;ID |No||
|combat_health_heal_friendly_team_effects|Effect&nbsp;ID |No||
|combat_health_heal_friendly_team_random_effects|Effect&nbsp;ID |No||
|combat_start_apply_limit|1...2|No||
|combat_start_apply_limit_effects|Effect&nbsp;ID |Yes||
|combat_start_effects|Effect&nbsp;ID |Yes||
|combat_stress_damage_apply_limit|1...1|No||
|combat_stress_damage_apply_limit_effects|Effect&nbsp;ID |Yes||
|combat_stress_damage_effects|Effect&nbsp;ID |Yes||
|combat_stress_damage_enemy_team_effects|Effect&nbsp;ID |No||
|combat_stress_damage_friendly_team_effects|Effect&nbsp;ID |No||
|combat_stress_heal_effects|Effect&nbsp;ID |No||
|combat_stress_heal_enemy_team_effects|Effect&nbsp;ID |No||
|combat_stress_heal_friendly_team_effects|Effect&nbsp;ID |No||
|death_effects|Effect&nbsp;ID |Yes||
|deaths_door_enter_effects|Effect&nbsp;ID |Yes||
|deaths_door_exit_effects|Effect&nbsp;ID |Yes||
|deaths_door_survive_effects|Effect&nbsp;ID |No||
|enemy_death_effects|Effect&nbsp;ID |No||
|enemy_death_team_effects|Effect&nbsp;ID |Yes||
|enemy_team_apply_limit|1...1|No||
|enemy_team_apply_limit_effects|Effect&nbsp;ID |Yes||
|enemy_team_effects|Effect&nbsp;ID |Yes||
|enemy_team_member_random_effects|Effect&nbsp;ID |Yes||
|enter_biome_effects|Effect&nbsp;ID |No||
|friendly_death_effects|Effect&nbsp;ID |Yes||
|friendly_death_team_effects|Effect&nbsp;ID |No||
|friendly_team_effects|Effect&nbsp;ID |Yes||
|inn_start_effects|Effect&nbsp;ID |No||
|kingdom_cleanse_effects|Effect&nbsp;ID |Yes||
|kingdom_contagion_effects|Effect&nbsp;ID |No||
|move_apply_limit|1...1|No||
|move_apply_limit_effects|Effect&nbsp;ID |Yes||
|move_effects|Effect&nbsp;ID |Yes||
|move_enemy_apply_limit|1...1|No||
|move_enemy_apply_limit_effects|Effect&nbsp;ID |Yes||
|move_enemy_effects|Effect&nbsp;ID |Yes||
|move_friendly_effects|Effect&nbsp;ID |No||
|node_before_effects|Effect&nbsp;ID |No||
|node_execute_started_effects|Effect&nbsp;ID |Yes||
|on_attack_as_performer_to_performer_effects|Effect&nbsp;ID |No||
|on_attack_as_performer_to_target_effects|Effect&nbsp;ID |No||
|on_attack_as_target_to_performer_apply_limit|1...1|No||
|on_attack_as_target_to_performer_apply_limit_effects|Effect&nbsp;ID |Yes||
|on_attack_as_target_to_performer_effects|Effect&nbsp;ID |Yes||
|on_attack_as_target_to_target_effects|Effect&nbsp;ID |No||
|on_crit_as_performer_to_performer_effects|Effect&nbsp;ID |Yes||
|on_crit_as_performer_to_target_effects|Effect&nbsp;ID |Yes||
|on_crit_as_target_to_performer_effects|Effect&nbsp;ID |No||
|on_crit_as_target_to_target_apply_limit|1...1|No||
|on_crit_as_target_to_target_apply_limit_effects|Effect&nbsp;ID |Yes||
|on_crit_as_target_to_target_effects|Effect&nbsp;ID |No||
|on_hit_as_performer_to_performer_apply_limit|1...2|No||
|on_hit_as_performer_to_performer_apply_limit_effects|Effect&nbsp;ID |Yes||
|on_hit_as_performer_to_performer_effects|Effect&nbsp;ID |Yes||
|on_hit_as_performer_to_target_apply_limit|1...2|No||
|on_hit_as_performer_to_target_apply_limit_effects|Effect&nbsp;ID |Yes||
|on_hit_as_performer_to_target_effects|Effect&nbsp;ID |Yes||
|on_hit_as_target_to_performer_apply_limit|1...1|No||
|on_hit_as_target_to_performer_apply_limit_effects|Effect&nbsp;ID |Yes||
|on_hit_as_target_to_performer_effects|Effect&nbsp;ID |No||
|on_hit_as_target_to_target_apply_limit|1...1|No||
|on_hit_as_target_to_target_apply_limit_effects|Effect&nbsp;ID |Yes||
|on_hit_as_target_to_target_effects|Effect&nbsp;ID |Yes||
|on_kill_as_performer_to_performer_effects|Effect&nbsp;ID |Yes||
|on_kill_as_target_to_performer_apply_limit|1...1|No||
|on_kill_as_target_to_performer_apply_limit_effects|Effect&nbsp;ID |No||
|on_kill_as_target_to_performer_effects|Effect&nbsp;ID |No||
|on_miss_as_performer_to_performer_effects|Effect&nbsp;ID |No||
|on_miss_as_performer_to_target_effects|Effect&nbsp;ID |No||
|on_miss_as_target_to_performer_effects|Effect&nbsp;ID |No||
|on_miss_as_target_to_target_effects|Effect&nbsp;ID |Yes||
|on_not_crit_as_performer_to_performer_effects|Effect&nbsp;ID |No||
|on_not_crit_as_performer_to_target_effects|Effect&nbsp;ID |Yes||
|on_overstress_effects|Effect&nbsp;ID |Yes||
|on_release_per_round_captured_effects|Effect&nbsp;ID |No||
|on_release_per_turn_captured_effects|Effect&nbsp;ID |Yes||
|performer_after_target_apply_limit|1...4|No||
|performer_after_target_apply_limit_effects|Effect&nbsp;ID |Yes||
|performer_after_target_effects|Effect&nbsp;ID |Yes||
|performer_apply_limit|1...3|No||
|performer_apply_limit_effects|Effect&nbsp;ID |Yes||
|performer_effects|Effect&nbsp;ID |Yes||
|performer_from_target_apply_limit|1...1|No||
|performer_from_target_apply_limit_effects|Effect&nbsp;ID |Yes||
|performer_from_target_effects|Effect&nbsp;ID |Yes||
|performer_neighbor_random_effects|Effect&nbsp;ID |No||
|performer_neighbors_effects|Effect&nbsp;ID |Yes||
|performer_on_crit_single_effects|Effect&nbsp;ID |Yes||
|performer_on_kill_fail_effects|Effect&nbsp;ID |Yes||
|performer_per_crit_effects|Effect&nbsp;ID |Yes||
|performer_per_target_effects|Effect&nbsp;ID |Yes||
|performer_team_effects|Effect&nbsp;ID |Yes||
|performer_team_others_apply_limit|1...1|No||
|performer_team_others_apply_limit_effects|Effect&nbsp;ID |Yes||
|performer_team_others_effects|Effect&nbsp;ID |Yes||
|performer_team_others_member_random_effects|Effect&nbsp;ID |No||
|respawn_effects|Effect&nbsp;ID |Yes||
|rest_item_effects|Effect&nbsp;ID |No||
|roster_status_exit_effects|Effect&nbsp;ID |Yes||
|round_end_effects|Effect&nbsp;ID |Yes||
|round_start_apply_limit|1...3|No||
|round_start_apply_limit_effects|Effect&nbsp;ID |Yes||
|round_start_effects|Effect&nbsp;ID |Yes||
|spawn_apply_limit|1...1|No||
|spawn_apply_limit_effects|Effect&nbsp;ID |Yes||
|spawn_effects|Effect&nbsp;ID |Yes||
|target_apply_limit|1...2|No||
|target_apply_limit_effects|Effect&nbsp;ID |Yes||
|target_effects|Effect&nbsp;ID |Yes||
|target_neighbor_random_effects|Effect&nbsp;ID |No||
|target_neighbors_apply_limit|1...1|No||
|target_neighbors_apply_limit_effects|Effect&nbsp;ID |Yes||
|target_neighbors_effects|Effect&nbsp;ID |No||
|target_team_effects|Effect&nbsp;ID |No||
|target_team_hit_member_random_effects|Effect&nbsp;ID |Yes||
|target_team_member_random_effects|Effect&nbsp;ID |No||
|target_team_others_effects|Effect&nbsp;ID |Yes||
|turn_end_apply_limit|1...2|No||
|turn_end_apply_limit_effects|Effect&nbsp;ID |Yes||
|turn_end_effects|Effect&nbsp;ID |Yes||
|turn_end_enemy_team_effects|Effect&nbsp;ID |No||
|turn_end_friendly_team_effects|Effect&nbsp;ID |No||
|turn_skip_effects|Effect&nbsp;ID |No||
|turn_start_apply_limit|1...1|No||
|turn_start_apply_limit_effects|Effect&nbsp;ID |Yes||
|turn_start_effects|Effect&nbsp;ID |Yes||
|turn_start_enemy_team_effects|Effect&nbsp;ID |No||
|turn_start_enemy_team_random_effects|Effect&nbsp;ID |No||
|turn_start_friendly_team_effects|Effect&nbsp;ID |No||

</details>

<details>
<summary>ActorDataExternalBuffs</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|buffs|Buff&nbsp;ID |Yes||
|instance_buffs|Example: instance_buffs,1,&#8203;deaths_head_on_enter_dd_01,&#8203;deaths_head_on_enter_dd_02,&#8203;deaths_head_on_enter_dd_03,&#8203;deaths_head_on_enter_dd_04,|Yes|When an Infernal Flame or a trinket appears in game, it can acquire random buffs until the end of a run|

</details>

<details>
<summary>ActorDataMode</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_BarkOverrideKey|bark_abomination_beast|No||

</details>

<details>
<summary>ActorDataPath</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ActorClassIds|<sub>parse fail</sub>|No||
|m_ActorClassTags|Tags|No||
|m_OrderPriority|1...3|No||
|m_Tags|Tags|Yes||
|m_UnlockId|<sub>parse fail</sub>|No||
|m_ViewedByDefault|Boolean|No||

</details>

<details>
<summary>ActorDataRunGoals</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|run_goals|RunGoal&nbsp;ID |No||

</details>

<details>
<summary>ActorDataSkill</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|launch_ranks|1...4|Yes|Ranks on which this skill can be used. I guess if its actor occupies several ranks, only the rank closest to the front counts.|
|m_ActorDataEffectsId|ActorDataEffects&nbsp;ID |No|Only used in forced skills.|
|m_ActorDataModeId|ActorDataMode&nbsp;ID |No||
|m_AdditionalDamageActorType|PERFORMER<br>TARGET<br>TARGET_NEIGHBOR_FRONT|No||
|m_AdditionalDamageValueMultiplier|0.50...2.00|No||
|m_AdditionalDamageValueString|dot|No||
|m_AdditionalDamageValueType|DOT_TAG_TOTAL_HEALTH_DAMAGE_OVER_TIME|No||
|m_AllConditionIds|Condition&nbsp;ID |Yes|Conjunctive conditioning. If any of its conditions fail, this skill becomes unavailable.|
|m_AnyConditionIds|Condition&nbsp;ID |Yes|Disjunctive conditioning. If all of its conditions fail, this skill becomes unavailable.|
|m_AverageRankIgnored|Boolean|No||
|m_CanBeRiposted|Boolean|No||
|m_ConditionIdOverride|ActorDataSkill&nbsp;ID |No||
|m_Cooldown|0...9|No||
|m_DeathClassTagIgnores|Tags|No|If used, enemies killed by this skill will not leave corpses|
|m_HideIfNotValid|Boolean|No||
|m_HideInvalidSkillTargetValidityTypes|invalid_condition|No||
|m_IgnoreDamageMultipliers|Boolean|No||
|m_IsActOut|Boolean|No||
|m_IsAdditionalEffectsValid|Boolean|No||
|m_IsAlwaysCooldownUpdating|Boolean|No||
|m_IsAlwaysEquipped|Boolean|No||
|m_IsAlwaysInput|Boolean|No||
|m_IsAlwaysTargetable|Boolean|No||
|m_IsAutoSelectSelfTarget|Boolean|No||
|m_IsBlockPass|Boolean|No||
|m_IsForced|Boolean|No||
|m_IsFreeAction|Boolean|No||
|m_IsFriendly|Boolean|No||
|m_IsFriendlySelfTargetValid|Boolean|No||
|m_IsLootWindowVisible|Boolean|No||
|m_IsMoveToTarget|Boolean|No||
|m_IsMultiHit|Boolean|No||
|m_IsOnlySelfTargetValid|Boolean|No||
|m_IsRiposteDamaging|Boolean|No|Used in riposte skills. If set to True, this riposte skill is activated whenever its actor is damaged.|
|m_IsRiposteNonDamaging|Boolean|No|Used in riposte skills. If set to True, this riposte skill is activated whenever its actor targeted.|
|m_IsStallInvalidating|Boolean|No||
|m_IsStartCooldownOnValidMode|Boolean|No||
|m_IsStressTriggerValid|Boolean|No||
|m_IsTokenViewVisible|Boolean|No||
|m_LaunchRanks|0...3|Yes||
|m_Limit|1...4|No||
|m_MatchingSkillIds|ActorDataSkill&nbsp;ID |Yes||
|m_ModeLinkedActorDataSkillId|<sub>parse fail</sub>|No||
|m_MultiHitAllTargetsConditionIds|Condition&nbsp;ID |No||
|m_MultiHitTargetLimit|2...2|No||
|m_ProfileUnlockId|Unlock&nbsp;ID |No||
|m_RandomSelectChance|0.30...3.00|No||
|m_SkillHistoryIdOverride|ActorDataSkill&nbsp;ID |No||
|m_SkillModifierChanceModifiers|Example: `m_SkillModifierChanceModifiers,curse,3,`<br>Slot 1 values:<br>curse|Yes||
|m_Tags|Tags|Yes|Common skill tags: melee,ranged,heal,stress_heal|
|m_TargetRelativeRanks|-3...3|Yes||
|m_Type|end_round<br>start_round|No||
|m_ValidActOutTypes|skill_additional<br>skill_after<br>skill_before<br>skill_block|Yes||
|multi_hit_guaranteed_ranks|1...2|No||
|multi_hit_shared_token_ignores|TokenIgnore&nbsp;ID |No||
|performer_buffs|<sub>parse fail</sub>|Yes||
|target_buffs|Buff&nbsp;ID |Yes||
|target_ranks|1...4|Yes||
|token_ignores|TokenIgnore&nbsp;ID |Yes||

</details>

<details>
<summary>ActorDataSkillReplacement</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|skill_replacements|SkillReplacement&nbsp;ID |Yes||

</details>

<details>
<summary>ActorDataStats</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|add_stat|Example: `add_stat,wound_percent_max,-0.1,`<br>Slot 1 values:<br>crit_chance<br>health_damage_dealt_percent<br>kingdom_actor_travel_distance<br>kingdom_actor_travel_effect_chance<br>kingdom_wound_heal_multiplier<br>speed<br>wound_percent_max|Yes||
|add_stats|-99.00...999.00|Yes||
|key_map|<details><summary>Click&#8201;to&#8201;expand</summary>crit_chance<br>deaths_door_chance<br>health_damage<br>health_damage_dealt_mult_percent<br>health_damage_dealt_percent<br>health_damage_range<br>health_damage_received_percent<br>health_heal_dealt_percent<br>health_heal_percent_between_nodes<br>health_heal_received_percent<br>health_max<br>kingdom_actor_travel_distance<br>kingdom_actor_travel_effect_chance<br>route_choice_chance<br>speed_number_of_turns<br>stress_max<br>wound_percent_max<br></details>|Yes||
|multiply_stat|Example: `multiply_stat,kingdom_actor_travel_distance,-1,`<br>Slot 1 values:<br>kingdom_actor_travel_distance|Yes||
|multiply_stats|-1.00...1.00|No||
|sub_stat|Example: `sub_stat,resistance,death,0.04,`<br>Slot 1 values:<br><details><summary>Click&#8201;to&#8201;expand</summary>affinity_relationship_tag_chance_modifier<br>affinity_relationship_tag_extra_duration<br>dot_effect_value_dealt_change<br>dot_effect_value_dealt_multiplier<br>dot_effect_value_received_change<br>dot_effect_value_received_multiplier<br>dot_extra_duration_dealt<br>dot_extra_duration_received<br>effect_performer_chance_multiplier<br>health_heal_dealt_percent<br>health_heal_received_percent<br>inn_quirk_generation_chance_modifier<br>overstress_chance_modifier<br>resistance<br>resistance_ignore<br>rest_item_effect_chance_modifier<br>route_choice_preference</details><br>Slot 2 values:<br><details><summary>Click&#8201;to&#8201;expand</summary>Bridge<br>Cache<br>CreatureDen<br>Dungeon<br>Gate<br>HeroSelect<br>Hospital<br>Inn<br>Oasis<br>Store<br>StoryAssist<br>StoryCosmic<br>StoryCultist<br>StoryHero<br>StoryHeroReplacement<br>StoryResist<br>Unknown<br>WatchTower<br>abm_moribund_stress_multiplier<br>bleed<br>blight<br>burn<br>death<br>debuff<br>disease<br>food<br>horror<br>hot<br>meltdown<br>move<br>neg_inn_normal<br>neg_inn_rare<br>negative<br>positive<br>positivetoken<br>resolute<br>rest_item<br>skill<br>stress<br>stun</details>|Yes||

</details>

<details>
<summary>ActorEffectTrigger</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|effects|Effect&nbsp;ID |Yes||
|m_ActorCount|1...4|No||
|m_ActorEffectTriggerSourceType|performer<br>target|No||
|m_ActorEffectTriggerTargetType|enemy_team<br>friendly_team<br>neighbor<br>party<br>performer<br>target|No||
|m_ActorEffectType|<details><summary>Click&#8201;to&#8201;expand</summary>On_Crit_As_Performer_To_Performer<br>On_Kill_As_Performer_To_Performer<br>change_class<br>combat_start<br>combat_stress_damage<br>death<br>deaths_door_enter<br>deaths_door_survive<br>enemy_death<br>move<br>node_after<br>node_before<br>node_execute_started<br>on_attack_as_performer_to_performer<br>on_crit_as_performer_to_performer<br>on_crit_as_target_to_performer<br>on_hit_as_target_to_target<br>on_kill_as_performer_to_performer<br>on_miss_as_performer_to_performer<br>on_resist<br>performer<br>round_end<br>round_start<br>spawn<br>target<br>turn_end<br>turn_start<br></details>|No||
|m_ApplyLimit|1...2|No||
|m_ApplyTargetToSource|Boolean|No||
|m_IncludeSourceActor|Boolean|No||
|m_NeighborActorEffectTriggerSourceType|performer<br>target|No||
|m_NeighborBackCount|1...3|No||
|m_NeighborFrontCount|1...3|No||
|m_UseActorDataEffectsConditionCalculationInput|Boolean|No||

</details>

<details>
<summary>ActorStatus</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|enter_effects|Effect&nbsp;ID |No||

</details>

<details>
<summary>AffinityLeaningLevel</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_LeaningMax|0...20|No||
|m_LeaningMin|0...20|No||
|m_RelationshipTagChances|Example: `m_RelationshipTagChances,negative,0.9,positive,0,`<br>Slot 1 values:<br>negative|Yes||

</details>

<details>
<summary>AffinityRelationship</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Chance|1...2|No||
|m_Tags|Tags|No||
|skill_modifiers|SkillModifier&nbsp;ID |Yes||

</details>

<details>
<summary>AffinityTickTrigger</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |Yes||
|m_BarkSwapPerformerAndTarget|Boolean|No||
|m_Chance|0.00...1.00|No||
|m_IsTelegraphed|Boolean|No||
|m_LeaningChange|-2...1|No||
|m_RoleType|OBSERVING_PERFORMER<br>PARTICIPATING|No||
|m_SkillAttributeTags|Tags|No||
|m_SkillAttributes|buff_add<br>dot_remove<br>stress_heal<br>token_add<br>token_remove|No||
|m_SkillIsCrit|Boolean|No||
|m_SkillIsFriendly|Boolean|No||
|m_Type|banter<br>effect<br>follow_up<br>health_heal<br>performer_moved<br>revenge<br>skill|No||
|performer_effects|Effect&nbsp;ID |No||

</details>

<details>
<summary>ArenaModifier</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|enter_actor_apply_limit_effects|Effect&nbsp;ID |Yes||
|enter_actor_effects|Effect&nbsp;ID |No||
|exit_actor_effects|Effect&nbsp;ID |No||
|m_ActorDataTags|Tags|No||
|m_Cooldown|1...1|No||
|m_DurationAmount|1...1|No||
|m_DurationType|round_end|No||
|m_EnterActorEffectsApplyLimit|1...1|No||

</details>

<details>
<summary>BarkTrigger</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Chance|0.05...100.00|No||
|m_DisplayType|negative<br>neutral<br>positive|No||
|m_Limit|1...2|No||
|m_Priority|1...1|No||
|m_RoleType|OBSERVING_PERFORMER<br>OBSERVING_TARGET<br>PERFORMER<br>TARGET|No||
|m_Tags|Tags|Yes||
|m_Type|<details><summary>Click&#8201;to&#8201;expand</summary>ALLY_DEATH<br>ARENA_MODIFIER_START<br>ARENA_MODIFIER_STOP<br>DEATHS_DOOR_SURVIVE<br>DOT_APPLIED<br>INN_STARTED<br>ITEM_APPLIED<br>OVERSTRESS<br>ROUTE_TRIGGERED<br>SKILL_CALCULATED_HIT<br>SKILL_CRIT<br>SKILL_MOVE_BACK<br>STALL<br>STATUS_ENTER<br>STRESS_DAMAGE<br>TORCH_DECREASE<br></details>|No||

</details>

<details>
<summary>BattleConfiguration</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|actorless_effects|Effect&nbsp;ID |Yes||
|actorless_round_start_effects|Effect&nbsp;ID |No||
|end_actor_all_conditions|Condition&nbsp;ID |No||
|hero_effects|Effect&nbsp;ID |No||
|m_AdditionalBattleConfigurationTableId|BattleConfigurationTable&nbsp;ID |No||
|m_BackgroundSceneOverride|<details><summary>Click&#8201;to&#8201;expand</summary>combat_arena_catacombs_creature_den<br>combat_arena_caves_creature_den<br>combat_arena_city_creature_den<br>combat_arena_city_dungeon_exterior<br>combat_arena_city_dungeon_interior<br>combat_arena_coast_creature_den<br>combat_arena_coast_dungeon_exterior<br>combat_arena_coast_dungeon_interior<br>combat_arena_farm_creature_den<br>combat_arena_farm_dungeon_exterior<br>combat_arena_farm_dungeon_interior<br>combat_arena_forest_creature_den<br>combat_arena_forest_dungeon_exterior<br>combat_arena_forest_dungeon_interior<br>combat_arena_hero_story_abomination_origin_1<br>combat_arena_hero_story_abomination_origin_2<br>combat_arena_hero_story_crusader_origin_1<br>combat_arena_hero_story_crusader_origin_2<br>combat_arena_hero_story_duelist_origin_1<br>combat_arena_hero_story_duelist_origin_2<br>combat_arena_hero_story_flagellant_origin_1<br>combat_arena_hero_story_graverobber_origin_1<br>combat_arena_hero_story_graverobber_origin_2<br>combat_arena_hero_story_hellion_origin_1<br>combat_arena_hero_story_hellion_origin_2<br>combat_arena_hero_story_highwayman_origin_1<br>combat_arena_hero_story_highwayman_origin_2<br>combat_arena_hero_story_jester_origin_1<br>combat_arena_hero_story_jester_origin_2<br>combat_arena_hero_story_leper_origin_1<br>combat_arena_hero_story_leper_origin_2<br>combat_arena_hero_story_manatarms_origin_1<br>combat_arena_hero_story_manatarms_origin_2<br>combat_arena_hero_story_occultist_origin_1<br>combat_arena_hero_story_occultist_origin_2<br>combat_arena_hero_story_plaguedoctor_origin_1<br>combat_arena_hero_story_plaguedoctor_origin_2<br>combat_arena_hero_story_runaway_origin_1<br>combat_arena_hero_story_runaway_origin_2<br>combat_arena_hero_story_vestal_origin_1<br>combat_arena_hero_story_vestal_origin_2<br>combat_arena_mountain_boss_arms<br>combat_arena_mountain_boss_body<br>combat_arena_mountain_boss_brain<br>combat_arena_mountain_boss_eyes<br>combat_arena_mountain_boss_lungs<br>combat_arena_stressworld<br>combat_arena_tundra_creature_den<br>combat_arena_tundra_dungeon_exterior<br>combat_arena_tundra_dungeon_interior<br>combat_arena_valley_barricade_gang_beastmen<br>combat_arena_valley_barricade_gang_courtier<br>combat_arena_valley_barricade_gang_coven<br></details>|No||
|m_BattleModifierOverrideId|BattleModifier&nbsp;ID |No||
|m_Chance|1...1|No||
|m_CompleteLootTables|LootTable&nbsp;ID |Yes||
|m_CompleteStoryLootTables|LootTable&nbsp;ID |No||
|m_EndActorConditionClassIds|<sub>parse fail</sub>|No||
|m_EndAtMaxStress|Boolean|No||
|m_EndConditionsIsComplete|Boolean|No||
|m_EndIsAlwaysComplete|Boolean|No||
|m_EndSequenceDelay|5...5|No||
|m_EnemyActors|<sub>parse fail</sub>|Yes||
|m_EnemyRandomOrder|Boolean|No||
|m_EnemySummonControllerConfigurationId|SummonControllerConfiguration&nbsp;ID |No||
|m_HasEndSequence|Boolean|No||
|m_IncompleteLootTables|LootTable&nbsp;ID |No||
|m_IncompleteStoryLootTables|LootTable&nbsp;ID |No||
|m_IsNextBattleOptional|Boolean|No||
|m_IsRollBattleModifier|Boolean|No||
|m_IsStallInvalidating|Boolean|No||
|m_NextBattleConfigurationId|BattleConfiguration&nbsp;ID |No||
|m_NextBattleConfigurationTableId|BattleConfigurationTable&nbsp;ID |No||
|m_PlayerActors|<sub>parse fail</sub>|Yes||
|m_ResultActors|<sub>parse fail</sub>|No||
|m_RoundLimit|6...6|No||
|m_RunDataStatsId|RunDataStats&nbsp;ID |No||
|m_RunLimit|1...1|No||
|m_Tags|Tags|Yes||
|m_TokenViewValid|Boolean|No||
|m_TorchOverride|no_torch|No||
|m_endBossCinematicName|EndBossVictory|No||

</details>

<details>
<summary>BattleConfigurationTable</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_chances|0...9999|Yes||
|m_conditions|Condition ID|Yes||
|m_ids|nothing|Yes||
|m_tags|Tags|Yes||
|m_types|battle_config<br>nothing<br>sub_table|Yes||

</details>

<details>
<summary>BattleModifier</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |Yes||
|m_Chance|0...1|No||
|m_Tags|Tags|No||
|m_TeamActorLimit|1...1|No||

</details>

<details>
<summary>Biome</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_BiomeGroupTag|Tags|No||
|m_DisabledRunValueTypes|Resist&nbsp;ID |No||
|m_InnTable|<sub>parse fail</sub>|No||
|m_RequiredStageCoachItemSlotType|Trophy|No||
|m_StoryDefaultBattleConfigurationTable|BattleConfigurationTable&nbsp;ID |No||
|road_events|RoadEvent&nbsp;ID |Yes||
|routes|Route&nbsp;ID |Yes||

</details>

<details>
<summary>BiomeGoal</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|invalid_biome_modifiers|<sub>parse fail</sub>|No||
|m_Chance|0...1|No||
|m_CompleteThresholdAmount|1...4|No||
|m_CompleteThresholdType|GREATER_THAN_OR_EQUAL|No||
|m_FailThresholdAmount|1...40|No||
|m_FailThresholdType|GREATER_THAN<br>GREATER_THAN_OR_EQUAL<br>LESS_THAN|No||
|m_LootId|LootTable&nbsp;ID |No||
|m_NumberOfTypicalBiomesMin|2...2|No||
|m_ShowCountProgressInDriving|Boolean|No||
|m_Type|BATTLE_FINISHED_SOURCE<br>BATTLE_STARTED_SOURCE<br>NODE_VISITED<br>RUN_VALUE<br>STAGE_COACH_ITEM_EQUIPPED|No||
|m_TypeStrings|CreatureDen<br>General<br>Hospital<br>Oasis<br>Store<br>StoryAssist<br>StoryCosmic<br>StoryCultist<br>WatchTower<br>barricade<br>dungeon<br>repair<br>story_resist<br>torch|Yes||
|m_ValidBiomeTypes|Biome&nbsp;ID |Yes||

</details>

<details>
<summary>BiomeKillContract</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Chance|2...3|No||
|m_CombatSource|story_resist|No||
|m_LootIds|LootTable&nbsp;ID |No||
|m_MaxDuration|7...7|No||
|m_MinDuration|3...5|No||
|m_OverrideBattleConfigurationTableId|BattleConfigurationTable&nbsp;ID |No||
|m_ValidBiomeTypes|city<br>coast<br>farm<br>forest<br>tundra|No||

</details>

<details>
<summary>BiomeModifier</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Chance|0...1|No||
|m_InfectionCooldownDays|100...100|No||
|m_InnUpgradeIds|InnUpgrade&nbsp;ID |Yes||
|m_LastsForever|Boolean|No||
|m_RoadEventIds|RoadEvent&nbsp;ID |No||
|m_SpreadChance|1...1|No||
|m_SpreadDistance|1...1|No||
|m_SpreadNumberMax|1...1|No||
|m_SpreadNumberMin|1...1|No||
|m_Tags|Tags|Yes||
|m_ValidBiomeTypes|Biome&nbsp;ID |Yes||

</details>

<details>
<summary>BiomeStatus</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_DurationAmount|3...3|No||
|m_DurationType|inn_start|No||
|m_Tags|Tags|No||

</details>

<details>
<summary>BiomeUpgrade</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Tags|Tags|No||

</details>

<details>
<summary>Boss</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|boss_modifiers|BossModifier&nbsp;ID |Yes||
|doom_reset_actorless_effects|Effect&nbsp;ID |Yes||
|doom_reset_hero_effects|Effect&nbsp;ID |No||
|m_AcademicsHonorariumLimit|5...5|No||
|m_EndBiomeType|Biome&nbsp;ID |No||
|m_IntroNarrationId|NarrationEntry&nbsp;ID |No||
|m_IsExtendedById|<sub>parse fail</sub>|No||
|m_IsRunGoalGenerating|Boolean|No||
|m_OrderedMidNarrationIds|NarrationEntry&nbsp;ID |Yes||
|m_OutroNarrationId|NarrationEntry&nbsp;ID |No||
|m_PrefabSubdirectoryId|Ambition<br>Cowardice<br>Denial<br>Obsession<br>Prologue<br>Resentment|No||
|m_PrerequisiteBossVictoryIds|<sub>parse fail</sub>|No||
|m_RecurringMidNarrationIds|NarrationEntry&nbsp;ID |Yes||
|m_SelectBiomeType|NarrationEntry&nbsp;ID |No||
|m_TorchLevelGroupId|<sub>parse fail</sub>|No||

</details>

<details>
<summary>BossModifier</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ActorDataEffectsId|ActorDataEffects&nbsp;ID |No||
|m_ActorDataTags|Tags|Yes||
|m_Chance|0.00...1.00|No||
|m_DataExternalBuffsId|DataExternalBuffs&nbsp;ID |No||
|m_NumberOfTypicalBiomesMax|1...3|No||
|m_NumberOfTypicalBiomesMin|1...3|No||

</details>

<details>
<summary>Buff</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ConditionId|Condition&nbsp;ID |Yes|Multiple values are used in the add_coven_glamer_buff buff|
|m_DurationAmount|1...5|No||
|m_DurationType|combat_end<br>embark_end<br>infinite<br>inn_start<br>performer_turn_end<br>performer_turn_start<br>round_end<br>round_start<br>skill_calculate<br>token_calculate_damage|No||
|m_InstanceLimit|1...66|No||
|m_IsVisible|Boolean|No||
|m_RemoveIfConditionNotMet|Boolean|No||
|m_SkillBlockId|SkillBlock&nbsp;ID |No||
|m_Tags|Tags|Yes||
|m_UnlockId|Unlock&nbsp;ID |No||
|m_showPopText|Boolean|No||
|token_ignores|TokenIgnore&nbsp;ID |No||

</details>

<details>
<summary>CinematicSubtitles</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_cinematicName|BossSelect<br>EndBossVictory|No||
|m_locKey|<details><summary>Click&#8201;to&#8201;expand</summary>vo_cinematic_denial_0<br>vo_cinematic_denial_1<br>vo_cinematic_denial_10<br>vo_cinematic_denial_2<br>vo_cinematic_denial_3<br>vo_cinematic_denial_4<br>vo_cinematic_denial_5<br>vo_cinematic_denial_6<br>vo_cinematic_denial_7<br>vo_cinematic_denial_8<br>vo_cinematic_denial_9<br>vo_cinematics_final_cinematic_01_0<br>vo_cinematics_final_cinematic_01_1<br>vo_cinematics_final_cinematic_01_10<br>vo_cinematics_final_cinematic_01_2<br>vo_cinematics_final_cinematic_01_3<br>vo_cinematics_final_cinematic_01_4<br>vo_cinematics_final_cinematic_01_5<br>vo_cinematics_final_cinematic_01_6<br>vo_cinematics_final_cinematic_01_7<br>vo_cinematics_final_cinematic_01_8<br>vo_cinematics_final_cinematic_01_9<br></details>|No||
|m_startTime|3.20...105.50|No||

</details>

<details>
<summary>Condition</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ActorIsNotSource|Boolean|No||
|m_ConditionActorType|MONSTERS<br>NONE<br>PARTY<br>PERFORMER<br>PERFORMER_NEIGHBOR_BACK<br>PERFORMER_NEIGHBOR_FRONT<br>TARGET<br>TARGET_NEIGHBOR_FRONT|No||
|m_ConditionMetTarget|Boolean|No||
|m_ConditionNumber|-0.25...999.00|No||
|m_ConditionNumberType|BOOL<br>EQUAL<br>GREATER_THAN<br>GREATER_THAN_OR_EQUAL<br>LESS_THAN<br>LESS_THAN_OR_EQUAL<br>MULTIPLE<br>PARAMETER|No||
|m_ConditionString|Depends on m_ConditionType|No||
|m_ConditionType|<details><summary>Click&#8201;to&#8201;expand</summary>actor_count_value<br>actor_stat_value<br>arena_modifier<br>battle_configuration_tag_count<br>biome<br>biome_count<br>biome_end_node<br>biome_history_count<br>biome_modifier_tag<br>biome_modifier_tag_count<br>biome_siege_strength<br>biome_status<br>biome_sub_type<br>biome_typical_count<br>boss<br>buff_tag_amount<br>class<br>combat_item_equipped<br>combat_source<br>day<br>doom_reset_count<br>dot_tag_amount<br>first_initiative<br>game_type<br>gang<br>health_percent<br>in_relationship_tag<br>incomplete_hero_story_choices_amount<br>inn_siege_resolve_visit<br>inn_tag<br>inn_upgrade<br>item_amount<br>item_equipped_tag<br>item_tag<br>item_tag_amount<br>item_total_percent<br>killed_class_amount<br>kingdom_class<br>last_initiative<br>mode<br>node<br>options_value_bool<br>overstress<br>party_class<br>path_tag_amount<br>profile_calculated_group_progress<br>profile_has_defeated_boss<br>profile_run_end_streak_failure<br>profile_unlock<br>profile_value<br>quest_complete<br>quest_step_complete<br>quest_step_current<br>quirk<br>quirk_tag_amount<br>rank<br>resist<br>resist_tag<br>roster_status<br>roster_status_amount<br>round<br>run_value<br>run_value_percent<br>siege_count<br>size<br>skill<br>skill_equipped<br>skill_equipped_tag<br>skill_received_history_amount<br>skill_received_history_last<br>skill_tag<br>skill_use_history_amount<br>skill_use_history_last<br>stage_coach_upgrade_equipped<br>stage_coach_upgrade_equipped_general_amount<br>stage_coach_upgrade_equipped_pet_amount<br>stage_coach_upgrade_equipped_tag<br>stage_coach_upgrade_equipped_trophy_amount<br>status<br>stress<br>stress_percent<br>tag<br>token_amount<br>token_tag_amount<br>turn<br></details>|No||
|m_IsInverse|Boolean|No||
|m_IsSkillConditionInputValid|Boolean|No||
|m_IsVisible|Boolean|No||
|m_SourceConditionActorType|PERFORMER|No||

</details>

<details>
<summary>Cost</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_AddedLocTag|Tags|No||
|m_IsItemEquipped|Boolean|No||
|m_ItemId|Item&nbsp;ID |No||
|m_ItemQty|1...1000|No||
|m_ItemTag|Tags|No||
|m_ProfileValue|1...50|No||
|m_ProfileValueType|Item&nbsp;ID |No||
|m_RunValue|1...40|No||
|m_RunValueType|hero_upgrade_points<br>torch|No||

</details>

<details>
<summary>DataAffinityTickTriggers</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|affinity_tick_triggers|AffinityTickTrigger&nbsp;ID |Yes||

</details>

<details>
<summary>DataExternalBuffs</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|buffs|Buff&nbsp;ID |Yes||

</details>

<details>
<summary>DataNodeReplacements</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|node_replacements|NodeReplacement&nbsp;ID |No||

</details>

<details>
<summary>DataStoryChoiceReplacements</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|story_choice_replacements|StoryChoiceReplacement&nbsp;ID |Yes||

</details>

<details>
<summary>DoomLevel</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_DoomMax|0...3|No||
|m_DoomMin|0...3|No||
|m_RunDataStatsId|RunDataStats&nbsp;ID |No||

</details>

<details>
<summary>Dot</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|effects|Effect&nbsp;ID |No||
|m_DurationAmount|2...98|No||
|m_DurationType|performer_turn_start|No||
|m_IgnoreEnemyDealtModifications|Boolean|No||
|m_IgnoreEnemyReceivedModifications|Boolean|No||
|m_IgnoreFriendlyDealtModifications|Boolean|No||
|m_IgnoreFriendlyReceivedModifications|Boolean|No||
|m_Tags|Tags|Yes||
|m_Type|bleed<br>blight<br>burn<br>horror<br>hot<br>taproot_strangle|No||

</details>

<details>
<summary>Effect</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |Yes||
|any_conditions|Condition&nbsp;ID |Yes||
|buffs|Buff&nbsp;ID |Yes||
|doom|1...5|No||
|escalation|1...3|No||
|m_AddTurn|0...1|No||
|m_AffinityLeaningChange|-10...10|No||
|m_ArenaModifierStartId|ArenaModifier&nbsp;ID |No||
|m_ArenaModifierStopId|ArenaModifier&nbsp;ID |No||
|m_BarkId|ID of a bark in localization files, for example: `herostory_abm_1_first_drink`|No||
|m_BiomeKillContractSpawnAmount|3...3|No||
|m_BiomeModifierId|<sub>parse fail</sub>|No||
|m_BiomeModifierSpawnRandom|1...1|No||
|m_BiomeStatusAddId|BiomeStatus&nbsp;ID |No||
|m_BuffRemoveAllTags|Tags|No||
|m_BuffRemoveAmount|1...99|No||
|m_BuffRemoveAmountRange|0...0|No||
|m_BuffRemoveRandom|Boolean|No||
|m_BuffRemoveTag|Tags|No||
|m_Capture|Boolean|No||
|m_Chance|0.00...1.00|No||
|m_ChanceMultiplierStatSubTypes|abm_moribund_stress_multiplier|No||
|m_ChancePerRoundSuffix|Boolean|No||
|m_ChangeClassActorId|<sub>parse fail</sub>|No||
|m_ChangeModeId|ActorDataMode&nbsp;ID |No||
|m_ClearSkillCooldowns|Boolean|No||
|m_ClearSkillUses|Boolean|No||
|m_ConditionId|Condition&nbsp;ID |No||
|m_CritChance|0.00...1.00|No||
|m_CritMultiplier|0.00...2.00|No||
|m_DotAddAmount|1...1|No||
|m_DotAddId|Dot&nbsp;ID |No||
|m_DotCopyAmount|99...99|No||
|m_DotCopyTags|Tags|No||
|m_DotGiveAmount|99...99|No||
|m_DotGiveTags|Tags|No||
|m_DotRemoveAllTypes|horror<br>hot<br>taproot_strangle|Yes||
|m_DotRemoveAmount|1...1|No||
|m_DotRemoveId|Dot&nbsp;ID |No||
|m_DotStealAmount|99...99|No||
|m_DotStealTags|Tags|No||
|m_HealthDamageAmount|1...30|No||
|m_HealthDamageDownToPercent|0.10...0.45|No||
|m_HealthDamagePercent|0.04...1.00|No||
|m_HealthHealAmount|1...40|No||
|m_HealthHealPercent|0.00...1.00|No||
|m_HealthHealPercentRange|0.05...0.66|No||
|m_HealthHealUpToPercent|0.25...1.00|No||
|m_HideHealPreview|Boolean|No||
|m_IgnoreDeathClass|Boolean|No||
|m_IgnoreResist|Boolean|No||
|m_IsAddTurnEndRound|Boolean|No||
|m_IsAddTurnValidOnExtraTurn|Boolean|No||
|m_IsAlwaysApply|Boolean|No||
|m_IsCombo|Boolean|No||
|m_IsKill|Boolean|No||
|m_IsLockedTeamPosition|Boolean|No||
|m_IsSourceOnly|Boolean|No||
|m_IsVisible|Boolean|No||
|m_LootIds|quest_courtier_creature_blood<br>quest_courtier_eldrich_blood<br>quest_courtier_prevent_spread_all<br>test_loot_table_1|Yes||
|m_LootReasonId|<details><summary>Click&#8201;to&#8201;expand</summary>alchemical_gear<br>ancestor_statue_crit<br>bundle_of_contracts<br>catacombs_salt_barrel<br>cave_scrounger_banter<br>chirurgeons_kit<br>city_scrounger_banter<br>courtier_blood_creature_infected_syringe<br>courtier_blood_creature_resilient_syringe<br>courtier_blood_eldrich_infected_syringe<br>courtier_blood_eldrich_resilient_syringe<br>courtier_blood_quest_syringe<br>courtier_cure_item_all<br>courtier_the_blood_syringe<br>explosives_magazine<br>farm_scrounger_banter<br>field_surgeon_banter<br>forest_scrounger_banter<br>griddle<br>mortar_and_pestle<br>pet_tick<br>quest_beastmen_medical_supplies<br>quest_beastmen_medicated_meat<br>quest_beastmen_nurses<br>quest_beastmen_survivors_tale<br>quest_courtier_collect_blood_sample<br>quest_courtier_creature_blood<br>quest_courtier_creature_blood_chc<br>quest_courtier_eldrich_blood<br>quest_courtier_eldrich_blood_chc<br>quest_courtier_formulate_cure_all<br>quest_courtier_fuel_reserves<br>quest_courtier_prevent_spread<br>quest_courtier_research_notes<br>quest_coven_charge_dagger_bleed<br>quest_coven_charge_dagger_blight<br>quest_coven_charge_dagger_burn<br>quest_coven_finger_bomb<br>quest_trophy_crusader_helmet_a<br>rummager_banter<br>shroud_scrounger_banter<br>stew_pot<br>stress_knitter_banter<br>tinkers_bench<br>trapmakers_kit<br>vermin_corpse_death<br>whiskey_still<br>worktable_loom<br></details>|No||
|m_Move|-10...3|No||
|m_MoveRange|2...2|No||
|m_Priority|-10...20|No||
|m_QuirkAddAmount|1...1|No||
|m_QuirkAddAmountRange|0...2|No||
|m_QuirkAddTag|Tags|No||
|m_QuirkRemoveAmount|1...99|No||
|m_QuirkRemoveAmountRange|0...2|No||
|m_QuirkRemoveIsLocked|Boolean|No||
|m_QuirkRemoveTag|Tags|No||
|m_Release|Boolean|No||
|m_RunValuesIsSetTo|Boolean|No||
|m_ShowValue|Boolean|No||
|m_Shuffle|Boolean|No||
|m_SiegeAllDelayChange|-1...3|No||
|m_SiegeAllStrengthChange|-2...3|No||
|m_SiegeSpawnAmount|1...4|No||
|m_SiegeSpawnAmountRange|2...2|No||
|m_SortType|CLASS_NAME<br>NAME|No||
|m_StageCoachUpgradeRemoveId|Item&nbsp;ID |No||
|m_StressDamage|0...10|No||
|m_StressDamageRange|3...3|No||
|m_StressHeal|1...10|No||
|m_StressHealDownFromMax|9...10|No||
|m_SummonAddToTurnOrderAfterCurrentTurnIndex|1...1|No||
|m_SummonClassActorId|<sub>parse fail</sub>|No||
|m_SummonIfRoom|Boolean|No||
|m_SummonLocationType|BACK<br>FRONT|No||
|m_TokenAddAmount|-1...5|No||
|m_TokenAddAmountRange|2...2|No||
|m_TokenAddId|Token&nbsp;ID |No||
|m_TokenAddTag|Tags|No||
|m_TokenConvertAmount|1...99|No||
|m_TokenConvertFromDotTags|Tags|No||
|m_TokenConvertFromTokenIds|Token&nbsp;ID |No||
|m_TokenConvertToId|Token&nbsp;ID |No||
|m_TokenCopyAmount|0...99|No||
|m_TokenCopyTags|Tags|No||
|m_TokenInvertAmount|1...99|No||
|m_TokenInvertAmountRange|99...99|No||
|m_TokenInvertIds|Token&nbsp;ID |Yes||
|m_TokenRemoveAmount|1...99|No||
|m_TokenRemoveId|vestal_flame|No||
|m_TokenRemoveRandom|Boolean|No||
|m_TokenRemoveTag|Tags|No||
|m_TokenStealAmount|1...99|No||
|m_TokenStealTags|Tags|No||
|m_TreasureAllDurationChange|3...3|No||
|m_TreasureSpawnAmount|3...3|No||
|m_UnlockRemoveNonSkillAmount|2...2|No||
|m_UnlockRemoveNonSkillAmountRange|1...1|No||
|m_UnlockRemoveUpgradedSkillAmount|3...3|No||
|m_UnlockRemoveUpgradedSkillAmountRange|2...2|No||
|m_WoundAddPercent|0.10...0.15|No||
|m_WoundRemovePercent|0.05...1.00|No||
|quirks|Quirk&nbsp;ID |No||
|stage_coach_armor|-1...1|No||
|stage_coach_wheels|-1...1|No||
|torch|-100...100|No||

</details>

<details>
<summary>ExtendedBoss</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|boss_modifiers|BossModifier&nbsp;ID |Yes||
|doom_reset_actorless_effects|Effect&nbsp;ID |No||
|doom_reset_hero_effects|Effect&nbsp;ID |No||
|m_AcademicsHonorariumLimit|5...5|No||
|m_EndBiomeType|Biome&nbsp;ID |No||
|m_IntroNarrationId|NarrationEntry&nbsp;ID |No||
|m_IsRunGoalGenerating|Boolean|No||
|m_OrderedMidNarrationIds|NarrationEntry&nbsp;ID |Yes||
|m_OutroNarrationId|NarrationEntry&nbsp;ID |No||
|m_PrefabSubdirectoryId|Denial<br>Resentment|No||
|m_RecurringMidNarrationIds|NarrationEntry&nbsp;ID |Yes||
|m_RequiredStageCoachItemSlotType|Trophy|No||
|m_SelectBiomeType|NarrationEntry&nbsp;ID |No||
|m_TorchLevelGroupId|<sub>parse fail</sub>|No||

</details>

<details>
<summary>Gang</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|escalation_torch_level_groups|TorchLevelGroup&nbsp;ID |Yes||
|m_BossBiomeType|Biome&nbsp;ID |No||
|m_Escalation2KingdomEventId|KingdomEvent&nbsp;ID |No||
|m_Escalation3KingdomEventId|KingdomEvent&nbsp;ID |No||
|m_IsReleased|Boolean|No||
|m_QuestId|<sub>parse fail</sub>|No||

</details>

<details>
<summary>Haptics</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_actorTags|Tags|Yes||
|m_audioSuffix|<details><summary>Click&#8201;to&#8201;expand</summary>_barricade<br>_barricade_cultist<br>_barricade_gaunt<br>_barricade_pillager<br>_combat_military<br>_focus<br>_meat<br>_meat_and_boxes<br>_pickup_01<br>_pickup_02<br>_pickup_03<br>_shared_barrel<br>_shared_crate<br>_shared_firewood<br>_shared_flame<br>_upgrade_milestone<br>_upgrade_milestone_max<br></details>|No||
|m_audioSuffixTags|Tags|Yes||
|m_audioTags|Tags|Yes||
|m_durationIds|HapticsDuration&nbsp;ID |Yes||
|m_intensityIds|HapticsIntensity&nbsp;ID |Yes||
|m_inventoryTags|Tags|Yes||
|m_skillUseTags|Tags|Yes||
|m_tags|Tags|Yes||

</details>

<details>
<summary>HapticsDeviceIntensity</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_devicePrefixes|DualSense<br>DualShock3<br>DualShock4<br>SwitchProControllerHID<br>XInputController<br>Xbox|Yes||
|m_intensity|1.00...1.00|No||

</details>

<details>
<summary>HapticsDisabledAudio</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_tags|Tags|Yes||

</details>

<details>
<summary>HapticsDuration</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_seconds|0.00...11.00|No||

</details>

<details>
<summary>HapticsIntensity</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_heartbeat1End|0.08...0.08|No||
|m_heartbeat1Start|0.00...0.00|No||
|m_heartbeat2End|0.38...0.38|No||
|m_heartbeat2Start|0.30...0.30|No||
|m_maxIntensity|0.05...1.00|No||
|m_minIntensity|0.10...0.25|No||
|m_period|1...1|No||
|m_type|constant<br>heartbeat<br>linear_down<br>linear_up<br>squared_down<br>squared_up<br>wave|No||

</details>

<details>
<summary>Inn</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|actorless_effects|Effect&nbsp;ID |No||
|hero_effects|Effect&nbsp;ID |Yes||
|kingdom_hero_effects|Effect&nbsp;ID |Yes||
|m_ActorDataPathChangeCostId|Cost&nbsp;ID |No||
|m_BonusLootTableIds|LootTable&nbsp;ID |Yes||
|m_DestroyedCampId|<sub>parse fail</sub>|No||
|m_HealthHealCostId|Cost&nbsp;ID |No||
|m_IgnoreVisitAllAchievement|Boolean|No||
|m_InnFeatureTypes|actor_path_change<br>fast_travel<br>physician<br>stage_coach_change_skin<br>stage_coach_repair<br>trainer<br>wainwright|Yes||
|m_InnRunDataStatsIds|RunDataStats&nbsp;ID |No||
|m_InnStartBarkActorDataIds|<sub>parse fail</sub>|No||
|m_InnUpgradeCategories|defense<br>physician<br>provisioner<br>trainer<br>wainwright|Yes||
|m_IsInnBonusValid|Boolean|No||
|m_LimitInnLevel|2...2|No||
|m_LimitInnUpgradeCategories|physician<br>provisioner<br>trainer<br>wainwright|Yes||
|m_NextBiomeRunDataStatsIds|<sub>parse fail</sub>|Yes||
|m_NumberOfBiomeChoices|0...2|No||
|m_QuirkGenerationAmount|0...1|No||
|m_QuirkGenerationChance|0.00...1.00|No||
|m_QuirkGenerationTags|Tags|Yes||
|m_StoreLootTableIds|LootTable&nbsp;ID |Yes||
|m_Tags|Tags|No||
|m_TemporaryInnUpgradeCategories|stage_coach_camp<br>stage_coach_inn|Yes||
|m_WoundHealCostId|Cost&nbsp;ID |No||
|run_value_transactions|<sub>parse fail</sub>|Yes||

</details>

<details>
<summary>InnBonus</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|actorless_effects|Effect&nbsp;ID |Yes||
|all_conditions|Condition&nbsp;ID |No||
|hero_effects|Effect&nbsp;ID |No||
|m_BonusLootTableIds|LootTable&nbsp;ID |Yes||
|m_DeliverableIcon|LootTable&nbsp;ID |No||
|m_InnRunDataStatsIds|RunDataStats&nbsp;ID |No||
|m_IsBonusLootExclusive|Boolean|No||
|m_QuestResource|<sub>parse fail</sub>|No||
|m_Score|4...4|No||

</details>

<details>
<summary>InnDataStats</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|add_stat|Example: `add_stat,kingdom_wound_heal_percentage,1,`<br>Slot 1 values:<br>defense<br>health_max<br>infection_adjacent_cure_percentage<br>kingdom_wound_heal_percentage<br>physician_wound_heal_percentage<br>siege_resolved_duration<br>siege_resolved_target_chance<br>siege_target_chance<br>storage_inventory_max_slots<br>unlock_skill_limit<br>upgrade_skill_limit|Yes||
|sub_stat|Example: `sub_stat,stage_coach_item_slot_equip_limit,General,4,`<br>Slot 1 values:<br>stage_coach_item_slot_equip_limit<br>Slot 2 values:<br>General<br>Pet<br>Trophy|Yes||

</details>

<details>
<summary>InnTable</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_chances|1...1|Yes||
|m_ids|Inn&nbsp;ID |Yes||
|m_types|inn|Yes||

</details>

<details>
<summary>InnUpgrade</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|actor_unlocks|Unlock&nbsp;ID |Yes||
|actorless_effects|Effect&nbsp;ID |Yes||
|biome_upgrades|BiomeUpgrade&nbsp;ID |Yes||
|hero_effects|Effect&nbsp;ID |Yes||
|kingdom_contagion_effects|Effect&nbsp;ID |No||
|kingdom_hero_effects|Effect&nbsp;ID |Yes||
|m_BonusLootTableIds|LootTable&nbsp;ID |No||
|m_InnFeatureTypes|actor_path_change<br>lock_positive_quirk<br>remove_disease<br>remove_negative_quirk<br>remove_positive_quirk|Yes||
|m_InnLevel|1...3|No||
|m_InnRunDataStatsIds|<sub>parse fail</sub>|No||
|m_InnUpgradeCategory|defense<br>physician<br>provisioner<br>trainer<br>wainwright|No||
|m_InnUpgradeType|major<br>minor<br>ultimate|No||
|m_IsBonusLootExclusive|Boolean|No||
|m_LevelSpriteIndex|1...3|No||
|m_OnPurchaseStoreLootTableIds|LootTable&nbsp;ID |Yes||
|m_Tags|Tags|Yes||
|prerequisite_all_inn_upgrades|<sub>parse fail</sub>|Yes||
|prerequisite_any_inn_upgrades|<sub>parse fail</sub>|Yes||

</details>

<details>
<summary>Item</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_DiscardGameScorePerQty|1...1|No||
|m_DurationAmount|1...1|No||
|m_DurationType|inn_end|No||
|m_InnUpgradeIds|InnUpgrade&nbsp;ID |Yes||
|m_IsStressTriggerBarking|Boolean|No||
|m_IsUnequipIfNotInParty|Boolean|No||
|m_IsUnequipInvalid|Boolean|No||
|m_OverrideBackgroundFileName|cru_quest|No||
|m_QuestResourceId|<sub>parse fail</sub>|No||
|m_QuestStepId|<sub>parse fail</sub>|No||
|m_RunEndGameScorePerQty|1...1|No||
|m_UnlockId|<sub>parse fail</sub>|No||
|m_applyLimitEffectIds|Effect&nbsp;ID |Yes||
|m_buyCostId|Cost&nbsp;ID |No||
|m_canDiscard|Boolean|No||
|m_combinable|Boolean|No||
|m_combinationApplyLimitEffectIds|Effect&nbsp;ID |Yes||
|m_combinationEffectApplyLimit|1...1|No||
|m_combinationEffectIds|Effect&nbsp;ID |No||
|m_conditionIds|Condition&nbsp;ID |Yes||
|m_effectApplyLimit|1...1|No||
|m_effectIds|Effect&nbsp;ID |Yes||
|m_forcedTargetActorDataId|<sub>parse fail</sub>|No||
|m_hideDamageAndCritTooltip|Boolean|No||
|m_hideInCollection|Boolean|No||
|m_hideRunDataStats|Boolean|No||
|m_isBuyHidden|Boolean|No||
|m_isConsumable|Boolean|No||
|m_isRandomTarget|Boolean|No||
|m_maxQty|1...40|No||
|m_numberOfTargets|1...4|No||
|m_partyEffectIds|Effect&nbsp;ID |No||
|m_possessionLimit|1...20|No||
|m_profileLevel|Effect&nbsp;ID |No||
|m_rewardLinkedTooltipVisible|Boolean|No||
|m_sellCostId|Cost&nbsp;ID |No||
|m_showTargettingInfoInTooltip|Boolean|No||
|m_slot|Flame<br>General<br>Pet<br>Trophy|No||
|m_tags|Tags|Yes||
|m_type|combat<br>currency<br>memory<br>rest<br>stage_coach_upgrade<br>trinket|No||
|m_useTagLimit|1...1|No||
|m_usedInCombat|Boolean|No||
|m_usedInDriving|Boolean|No|Unused field|
|m_usedInInn|Boolean|No||
|sub_type|ItemSubtype&nbsp;ID |No||

</details>

<details>
<summary>ItemBlock</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ItemIds|Item&nbsp;ID |Yes||

</details>

<details>
<summary>ItemSubtype</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_LootNarrationTag|Tags|No||
|m_MinRequiredCountLootNarrationIndex|0...1|No||
|m_SortPriority|0...4|No||
|m_TrinketEquipSfxOverrideEventPath|event:/ui/shared/trinket_equip_cultist|No||

</details>

<details>
<summary>KingdomDifficulty</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|actor_path_set_type|0...0|No||
|escalation_2_day|8...15|No||
|escalation_3_day|25...33|No||
|loss_day|45...72|No||
|loss_percentage_of_inns_destroyed|30...60|No||
|m_IsDefault|Boolean|No||
|m_RosterReplacementType|none<br>refill|No||
|roster_active_entry_limit|12...12|No||
|siege_run_stat_index|0...1|No||
|skill_set_type|0...1|No||
|start_free_treasures|1...2|No||
|start_siege_strength|3...3|No||

</details>

<details>
<summary>KingdomEvent</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |Yes||
|effects|Effect&nbsp;ID |Yes||
|inn_upgrades|InnUpgrade&nbsp;ID |No||
|m_BiomeModifierId|BiomeModifier&nbsp;ID |No||
|m_Chance|0.00...2.00|No||
|m_Cooldown|5...5|No||
|m_EffectRosterStatusTypes|party|Yes||
|m_EventTypeRarity|RARE|No||
|m_EventTypeRef|<details><summary>Click&#8201;to&#8201;expand</summary>almanac_city<br>almanac_coast<br>almanac_farm<br>almanac_forest<br>almanac_tundra<br>city<br>coast<br>escalation<br>farm<br>forerunner<br>forest<br>negative<br>positive<br>regent<br>tundra<br>wagonmaster<br>warmaster<br></details>|No||
|m_IsGeneratedInAdvance|Boolean|No||
|m_KingdomLimit|1...1|No||
|m_LootIds|LootTable&nbsp;ID |No||
|m_MinGenerationDay|2...7|No||
|m_Tags|Tags|No||

</details>

<details>
<summary>KingdomMap</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|biome+Boss|biome+Farm<br>biome+Forest|Yes||
|biome+Farm|biome+City<br>biome+Coast<br>biome+Forest|Yes||
|biome+Forest|biome+City<br>biome+Farm|Yes||
|boss|biome+Boss<br>biome+City<br>biome+Forest<br>biome+Tundra<br>boss<br>camp<br>inn+kingdom_inn<br>inn+kingdom_inn_fast_travel|Yes||
|inn+kingdom_inn|biome+City<br>biome+Coast<br>biome+Farm<br>biome+Forest<br>biome+Tundra<br>camp<br>inn+kingdom_inn<br>inn+kingdom_inn_fast_travel|Yes||
|inn+kingdom_inn_fast_travel|biome+City<br>biome+Farm<br>biome+Forest<br>biome+Tundra<br>camp<br>inn+kingdom_inn<br>inn+kingdom_inn_fast_travel|Yes||

</details>

<details>
<summary>KingdomSiegeAttack</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |No||
|m_DestroyChance|1...1|No||
|m_InnHealthDamage|90...90|No||
|m_RemoveRandomUpgradeAmount|2...2|No||
|m_RemoveRandomUpgradeChance|1...1|No||

</details>

<details>
<summary>KingdomSiegeDefense</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ActorClassIds|<sub>parse fail</sub>|Yes||

</details>

<details>
<summary>KingdomTreasure</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_LootIds|LootTable&nbsp;ID |No||
|m_MaxDuration|7...7|No||
|m_MaxInnLevel|1...3|No||
|m_MinDuration|4...4|No||
|m_MinInnLevel|0...3|No||
|m_TreasureLevel|1...3|No||

</details>

<details>
<summary>LootTable</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_chances|0.00...9999.00|Yes||
|m_conditions|<details><summary>Click&#8201;to&#8201;expand</summary>biome_greater_than_1+is_confessions<br>biome_less_than_or_equal_to_1+is_confessions<br>catacombs_biome_check+quest_courtier_current_step_collect_blood_sample<br>cave_biome_check+quest_courtier_current_step_collect_blood_sample<br>crusader_current_quest_not_step_6+crusader_current_quest_not_step_7<br>escalation_is_1+current_biome_is_valleykingdom<br>escalation_is_1+current_biome_not_valleykingdom<br>hero_party_has_bounty_hunter+is_kingdoms<br>is_confessions+biome_typical_equal_or_greater_than_3<br>is_confessions+biome_typical_less_than_or_equal_to_2<br>is_kingdoms+cave_biome_check<br>is_kingdoms+escalation_is_1<br>is_kingdoms+escalation_is_over_1<br>is_kingdoms+quest_beastmen_current_step_find_mauled_bodies<br>kingdom_gang_is_courtier+has_inn_upgrade_physician_medical_item_shop<br>kingdom_gang_is_courtier+quest_courtier_collect_resilient_blood_complete<br>kingdom_gang_is_courtier+quest_courtier_current_step_collect_resilient_blood<br>kingdom_gang_is_courtier+quest_courtier_current_step_collect_syringe<br>kingdom_gang_is_coven+escalation_is_1<br>kingdom_gang_is_coven+quest_coven_not_completed_step_assemble_witchbane_dagger<br>kingdom_inn_has_bounty_hunter+is_kingdoms<br>party_has_incomplete_hero_shrines+is_confessions<br>quest_coven_completed_step_assemble_witchbane_dagger+kingdom_gang_is_coven<br>quest_coven_completed_step_equip_boiled_head+kingdom_gang_is_coven+escalation_is_over_1+stagecoach_has_quest_coven_boiled_head_equipped<br>quest_coven_current_step_deliver_witch_fingers+is_road_combat_hidden<br></details>|Yes||
|m_ids|biome_reward<br>hero_upgrade_points<br>nothing<br>stage_coach_armor<br>stage_coach_wheels<br>torch|Yes||
|m_qtys|Example: `m_qtys,1,1,1,1,`<br>Slot 1 values:<br>[1-2]<br>[2-3]<br>[2-4]<br>[4-6]<br>Slot 2 values:<br>[1-2]<br>[12-24]<br>[2-4]|Yes|[1-2] means that one loot pull can return varied number (from 1 to 2) of items/sub-loot tables|
|m_tags|Tags|Yes||
|m_types|all_sub_table<br>biome_reward<br>exclusive_sub_table<br>item<br>nothing<br>provision<br>quest_step<br>sub_table<br>unique_sub_table|Yes||
|m_unlockId|<sub>parse fail</sub>|No||

</details>

<details>
<summary>NarrationEntry</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_allTags|Tags|Yes||
|m_anyTags|Tags|Yes||
|m_audioEventId|Example: `event:/vo/altar_of_hope/assign_memory_01`|No||
|m_avoidTags|Tags|Yes||
|m_chance|0.50...0.67|No||
|m_disabledGameTypes|Rules&nbsp;ID |No||
|m_guaranteeType|always<br>profile_first|No||
|m_maxOccurrences|1...2|Yes||
|m_numberOfPanels|0...7|No||
|m_occurrenceTypes|biome<br>combat<br>inn<br>node<br>profile<br>run|Yes||
|m_type|Rules&nbsp;ID |No||

</details>

<details>
<summary>NarrationType</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_chance|0.10...1.00|No||
|m_disabledGameTypes|Rules&nbsp;ID |No||
|m_maxOccurrences|1...3|Yes||
|m_occurrenceTypes|altar_of_hope<br>biome<br>combat<br>inn<br>node<br>run|Yes||

</details>

<details>
<summary>NodeDeliverable</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |No||
|m_LootIds|LootTable&nbsp;ID |No||
|m_NodeType|CreatureDen<br>Hospital<br>Oasis<br>Store<br>StoryAssist<br>StoryCosmic<br>Watchtower|No||
|m_Tags|Tags|No||

</details>

<details>
<summary>NodeReplacement</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_AdditionalEndNodeTypes|BeastmenAlpha|No||
|m_AdditionalStartNodeTypes|CreatureDen|No||
|m_FromNodeType|Guardian<br>StoryAssist|No||
|m_IsVisible|Boolean|No||
|m_NodeExitBarkOverrideNodeTypes|Gate|No||
|m_NodeExitBarkPreferredActorDataIds|<sub>parse fail</sub>|No||
|m_ToNodeType|CovenAssist<br>Warlord|No||
|m_ValidBiomeTypes|Biome&nbsp;ID |Yes||

</details>

<details>
<summary>Overstress</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|effects|Effect&nbsp;ID |Yes||
|m_Chance|0.20...1.00|No||
|m_LeaningChange|-3...2|No||
|m_ResetPathToDefault|Boolean|No||

</details>

<details>
<summary>Quest</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_QuestType|game|No||
|m_ValidGameTypes|expedition|No||
|on_completion_unlocks|Unlock&nbsp;ID |No||
|quest_steps|QuestStep&nbsp;ID |Yes||

</details>

<details>
<summary>QuestStep</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_DataNodeReplacementsId|DataNodeReplacements&nbsp;ID |No||
|m_DisplayOverrideId|inn_combined<br>inn_exclusive<br>start|No||
|m_InnLootIds|LootTable&nbsp;ID |No||
|m_IsKingdomTimelineValid|Boolean|No||
|m_QuestStepNumber|4...4|No||
|m_QuestStepString|quest_beastmen_rotting_dead_hidden|No||
|m_QuestStepType|inn_bonus<br>loot<br>stage_coach_upgrade_equip|No||
|m_SkipGuaranteedLootIds|LootTable&nbsp;ID |Yes||

</details>

<details>
<summary>Quirk</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|generation_all_conditions|Condition&nbsp;ID |No||
|m_DurationAmount|1...3|No||
|m_DurationType|day|No||
|m_EscalationTags|Tags|No||
|m_Rarity|NORMAL<br>RARE|No||
|m_ShowDescriptionExplicit|Boolean|No||
|m_ShowDescriptionFlavor|Boolean|No||
|m_Tags|Tags|Yes||

</details>

<details>
<summary>QuirkContainer</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|invalid_quirks|<sub>parse fail</sub>|No||
|m_IdGuaranteeGenerationLimits|Example: `m_IdGuaranteeGenerationLimits,quirk_kleptomania_neg,1,`<br>Slot 1 values:<br>quirk_kleptomania_neg|Yes||
|m_TagGenerations|Tags|Yes||
|m_TagLimits|Example: `m_TagLimits,positive,3,negative,3,disease,1,`<br>Slot 1 values:<br>positive|Yes||

</details>

<details>
<summary>Resist</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ActorStatSubType|Resist&nbsp;ID |No||
|m_ActorStatType|resistance|No||
|m_BuffTags|Tags|No||
|m_CritMod|-0.20...0.00|No||
|m_DotTags|Tags|No||
|m_IgnoreActorStatType|resistance_ignore|No||
|m_IgnorePopTextSourceTypes|skill|No||
|m_IsDeath|Boolean|No||
|m_IsStress|Boolean|No||
|m_Max|0.90...1.00|No||
|m_Min|0...0|No||
|m_PositiveRunValueTypes|Resist&nbsp;ID |No||
|m_QuirkTags|Tags|No||
|m_RunStatSubType|Resist&nbsp;ID |No||
|m_RunStatType|resistance|No||
|m_SkillAttributes|CAPTURE<br>MOVE|Yes||
|m_TokenIds|Token&nbsp;ID |Yes||
|m_TokenTags|Tags|Yes||

</details>

<details>
<summary>RoadEvent</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Chance|1...1|No||
|m_RoadEventCategory|Ambush<br>Banter<br>Objects|No||
|m_ValidGameType|expedition|No||

</details>

<details>
<summary>Route</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|actorless_effects|Effect&nbsp;ID |No||
|m_AllowsBark|Boolean|No||
|m_AllowsPetSqueal|Boolean|No||
|m_Chance|0...5|No||
|m_EndingRowsToSkip|1...1|No||
|m_OverrideNarrationTags|Tags|No||
|m_RouteType|gang_combat<br>hazard<br>oblivion_tear<br>rough_patch<br>safe|No||

</details>

<details>
<summary>Rules</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|actor_transfer_effects|Effect&nbsp;ID |Yes||
|boss_activate_any_conditions|Condition&nbsp;ID |Yes||
|boss_select_destination_any_conditions|Condition&nbsp;ID |Yes||
|disharmonious_effects|Effect&nbsp;ID |No||
|disharmonious_relationship_effects|Effect&nbsp;ID |No||
|general_slot_unlocks|<sub>parse fail</sub>|Yes||
|harmonious_effects|Effect&nbsp;ID |No||
|harmonious_relationship_effects|Effect&nbsp;ID |No||
|leaning_affinity_tick_trigger_chance_modifier|Example: `leaning_affinity_tick_trigger_chance_modifier,-3,0,False,0,`|Yes||
|m_ActorDataActOutId|<sub>parse fail</sub>|No||
|m_ActorTransferEffectMinDistance|1...1|No||
|m_AffinityRelationshipDuration|5...5|No||
|m_BattleEndMinHealthHealUpToPercent|0.20...0.20|No||
|m_CampAmbushBattleConfigTableId|BattleConfigurationTable&nbsp;ID |No||
|m_CampBaseId|<sub>parse fail</sub>|No||
|m_CritDamageMultiplications|1.00...1.50|Yes||
|m_CritDotExtraDuration|0...0|No||
|m_CureQuirkByTagCosts|Example: `m_CureQuirkByTagCosts,disease,12,`<br>Slot 1 values:<br>disease|Yes||
|m_DataAffinityTickTriggersId|<sub>parse fail</sub>|No||
|m_FirstKillNarrationMaxRound|2...2|No||
|m_FirstKingdomDefaultPartyActorClassIds|<sub>parse fail</sub>|Yes||
|m_GangBossTag|Tags|No||
|m_GeneralNumberOfSlots|1...1|No||
|m_HeroHurtBigNarrationHealthPercent|0.30...0.30|No||
|m_HeroSpecificDeathNarrationChance|0.65...0.65|No||
|m_InnBaseId|<sub>parse fail</sub>|No||
|m_InnInitialFreeUpgradeCounts|1...2|Yes||
|m_LeaningDurationCompleteChangeToStart|3...3|No||
|m_LeaningMax|20...20|No||
|m_LeaningMin|0...0|No||
|m_LeaningStart|9...10|No||
|m_LeaningStartReserve|7...10|No||
|m_LockQuirkByTagCosts|Example: `m_LockQuirkByTagCosts,positive,32,`<br>Slot 1 values:<br>positive|Yes||
|m_LogItemIds|Item&nbsp;ID |Yes||
|m_LogQuirkTags|Tags|Yes||
|m_LongCombatNarrationFirstRound|7...7|No||
|m_MaxRerollInventory|3...3|No||
|m_MemoryLootTableIds|LootTable&nbsp;ID |Yes||
|m_MemoryNumberOfSlots|5...5|No||
|m_NodeExecuteLootIds|LootTable&nbsp;ID |No||
|m_OptionalBiomeMinBiomeTypicalCount|1...1|No||
|m_PetNumberOfSlots|0...0|No||
|m_PointsMin|0...0|No||
|m_PointsProfileValueType|Item&nbsp;ID |No||
|m_RemoveQuirkByTagCosts|Example: `m_RemoveQuirkByTagCosts,negative,16,positive,16,`<br>Slot 1 values:<br>negative|Yes||
|m_RespawnStageCoachRefillRunValueTypes|stage_coach_armor<br>stage_coach_wheels<br>torch|Yes||
|m_RunDataStatsId|RunDataStats&nbsp;ID |No||
|m_SellExecutingNodeTypes|Store|No||
|m_SiegeCounterStartMax|100...100|No||
|m_SiegeCounterStartMin|100...100|No||
|m_SiegeKingdomTreasureId|KingdomTreasure&nbsp;ID |No||
|m_SiegeManualBattleConfigTableId|BattleConfigurationTable&nbsp;ID |No||
|m_SiegeMinGenerationDay|0...0|No||
|m_SiegeStrengthMax|10...10|No||
|m_SiegeStrengthMin|3...3|No||
|m_SkillModifierChanceBase|6...6|No||
|m_SkillModifierChancePerSkillUse|1...1|No||
|m_SkipIntroProfileValue|12...12|No||
|m_SkipIntroProfileValueType|Item&nbsp;ID |No||
|m_SkipValleyRunValues|Example: `m_SkipValleyRunValues,torch,100,`<br>Slot 1 values:<br>torch|Yes||
|m_StageCoachAdjacentBiomeRewardLootId|LootTable&nbsp;ID |No||
|m_StallInvalidatingThresholdPercent|0.60...0.60|No||
|m_StallMaxNumberOfEnemies|2...2|No||
|m_StallMinNumberOfHeroes|3...3|No||
|m_StallMinRound|3...3|No||
|m_StartingGold|0...40|No||
|m_StressPercentageThresholds|0.00...0.67|Yes||
|m_TreasureCounterStartMax|100...100|No||
|m_TreasureCounterStartMin|0...0|No||
|m_TrinketNumberOfSlots|2...2|No||
|m_TrophyNumberOfSlots|1...1|No||
|m_TurnOrderSpeedRollPerExtraAction|-2...-2|No||
|m_TurnOrderSpeedRollRangeMax|6...6|No||
|m_TurnOrderSpeedRollRangeMin|0...0|No||
|m_TurnOrderSpeedRollRound|Boolean|No||
|m_academicViewCombatLimit|2...2|No||
|m_academicViewRoundLimit|2...2|No||
|m_affinityTutorialLimit|3...3|No||
|m_banterStressChange|1...1|No||
|m_banterTickTriggerChance|0.50...0.50|No||
|m_banterTickTriggerLimit|2...2|No||
|m_betweenNodeAfterNodePercentage|0.25...0.25|No||
|m_betweenNodeBeforeNodePercentage|0.75...0.75|No||
|m_betweenNodeDeltaPercentage|0.40...0.40|No||
|m_betweenNodeMaxPercentage|0.90...0.90|No||
|m_betweenNodeMinPercentage|0.10...0.10|No||
|m_biomeBossTag|Tags|No||
|m_chanceOfRelationshipShift|0.50...0.50|No||
|m_chanceOfSeatShift|0...0|No||
|m_chanceOfStress|0.50...0.50|No||
|m_defaultSize|20...20|No||
|m_doomMaxTutorialLimit|4...4|No||
|m_doomTutorialLimit|1...1|No||
|m_drivingHealingPercentLimit|0.75...0.75|No||
|m_drivingInfoViewLimit|2...2|No||
|m_drivingWoundHeal|0.10...0.10|No||
|m_endBossTag|Tags|No||
|m_farSideRoadEventDistRatio|0.95...0.95|No||
|m_goldId|Item&nbsp;ID |No||
|m_heroReplacementMaxDist|5...5|No||
|m_heroReplacementMinDist|2...2|No||
|m_highThreatQty|1...1|No||
|m_innIntroLimit|2...2|No||
|m_inventoryFullPercentLimit|0.90...0.90|No||
|m_leaguesPerRow|10...10|No||
|m_lootInventoryIgnoresMaxQty|Boolean|No||
|m_lowTorchTutorialLimit|35...35|No||
|m_maxNegativeLeaning|-4...-4|No||
|m_minCandlesForLootNarration|1...1|No||
|m_minHeroPointsForLootNarration|1...1|No||
|m_minItemsForLootNarration|8...8|No||
|m_minPositiveLeaning|4...4|No||
|m_minRelicsForLootNarration|24...24|No||
|m_minStagecoachUpgradesForLootNarration|1...1|No||
|m_minTrinketCountsForLootNarration|1...1|Yes||
|m_noTorchTutorialLimit|0...0|No||
|m_nodeExitBarkChance|0.50...0.50|No||
|m_nodeExitBarkDelaySeconds|1.80...1.80|No||
|m_relationshipChanceOfSeatShift|0...0|No||
|m_relationshipChanceOfStress|0.40...0.40|No||
|m_roadEventRandomizationOffsetRatio|0.05...0.05|No||
|m_sideRoadEventDistRatio|0.47...0.47|No||
|m_stressTutorialLimit|5...5|No||
|m_torchBasicsTutorialLimit|60...60|No||
|m_trophiesTutorialBiomeEnterLimit|3...3|No||
|node_doom_effects|Effect&nbsp;ID |No||
|on_added_to_roster_effects|<sub>parse fail</sub>|No||
|pet_slot_unlocks|<sub>parse fail</sub>|No||
|repeatable_item|<details><summary>Click&#8201;to&#8201;expand</summary>combat<br>memory_reroll<br>repeatable_combat_cost_0<br>repeatable_combat_cost_1<br>repeatable_combat_cost_2<br>repeatable_combat_cost_3<br>repeatable_combat_cost_4<br>repeatable_combat_cost_5<br>repeatable_combat_cost_6<br>repeatable_items_combat<br>repeatable_items_rest<br>repeatable_items_stagecoach<br>repeatable_items_trinkets<br>repeatable_memory_reroll_cost_0<br>repeatable_memory_reroll_cost_1<br>repeatable_memory_reroll_cost_2<br>repeatable_memory_reroll_cost_3<br>repeatable_rest_cost_0<br>repeatable_rest_cost_1<br>repeatable_rest_cost_2<br>repeatable_rest_cost_3<br>repeatable_rest_cost_4<br>repeatable_rest_cost_5<br>repeatable_rest_cost_6<br>repeatable_stage_coach_upgrade_cost_0<br>repeatable_stage_coach_upgrade_cost_1<br>repeatable_stage_coach_upgrade_cost_2<br>repeatable_trinket_cost_0<br>repeatable_trinket_cost_1<br>repeatable_trinket_cost_2<br>rest<br>stage_coach_upgrade<br>trinket<br>unused_but_has_to_have_a_value_or_it_wont_parse_correctly<br></details>|Yes||
|reroll_quirks_costs|Cost&nbsp;ID |Yes||
|retreat_effects|Effect&nbsp;ID |No||
|retreat_per_hero_effects|Effect&nbsp;ID |No||
|retreat_single_hero_effects|Effect&nbsp;ID |No||
|route_choice_unwanted_effects|Effect&nbsp;ID |No||
|route_choice_wanted_effects|Effect&nbsp;ID |No||
|score_multiplier|Example: `score_multiplier,start_biomes_cleared,2,`<br>Slot 1 values:<br>academics_honorarium<br>faced_end_boss<br>first_end_boss_victory<br>heroes_hired<br>heroes_survived<br>inn_bonus<br>inventory_items<br>optional_biomes_cleared<br>run_goals_class<br>run_goals_path<br>start_biomes_cleared<br>victory|Yes||
|score_replacement|Example: `score_replacement,typical_biomes_cleared,12,24,36,`<br>Slot 1 values:<br>biome_bosses_cleared<br>typical_biomes_cleared|Yes||
|siege_loss_hero_effects|Effect&nbsp;ID |Yes||
|siege_run_data_stats|RunDataStats&nbsp;ID |Yes||
|stall_effects|Effect&nbsp;ID |No||
|stress_affinity_tick_trigger_chance_modifier|Example: `stress_affinity_tick_trigger_chance_modifier,0.75,1,False,0,`|Yes||
|trinket_slot_unlocks|Effect&nbsp;ID |No||
|trophy_slot_unlocks|Effect&nbsp;ID |No||

</details>

<details>
<summary>RunDataStats</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|add_stat|Example: `add_stat,map_generation_length_multiplier,0.4,`<br>Slot 1 values:<br><details><summary>Click&#8201;to&#8201;expand</summary>battle_modifier_chance<br>camp_ambush_chance<br>kill_contract_accrual<br>kill_contract_accrual_range<br>kill_contract_spawn_limit<br>kill_contract_spawn_threshold<br>kingdom_event_generation_chance<br>map_generation_length_multiplier<br>scout_node_chance<br>scout_route_chance<br>siege_accrual<br>siege_accrual_range<br>siege_delay<br>siege_delay_range<br>siege_spawn_limit<br>siege_spawn_threshold<br>siege_strength<br>siege_strength_range<br>treasure_accrual<br>treasure_accrual_range<br>treasure_spawn_threshold</details>|Yes||
|add_stats|-50.00...1000.00|Yes||
|key_map|<details><summary>Click&#8201;to&#8201;expand</summary>affinity_tick_trigger_negative_chance_multiplier<br>affinity_tick_trigger_positive_chance_multiplier<br>battle_modifier_chance<br>boss_modifier_chance_modifier<br>doom_default_value<br>doom_effect_number_of_nodes<br>doom_max_value<br>doom_min_value<br>doom_reset_value<br>escalation_default_value<br>escalation_max_value<br>escalation_min_value<br>hero_upgrade_points_default_value<br>hero_upgrade_points_max_value<br>hero_upgrade_points_min_value<br>hire_chance<br>hire_typical_biomes_max<br>hire_typical_biomes_min<br>map_generation_node_execute_loot_chance<br>map_generation_nodes_per_row_max<br>map_generation_nodes_per_row_min<br>player_inventory_max_slots<br>retreat_chance<br>run_generation_number_of_optional_biomes<br>run_generation_number_of_typical_biomes<br>run_generation_optional_biome_chance<br>score_bonus_multiplier<br>scout_node_chance<br>scout_route_chance<br>stage_coach_armor_default_value<br>stage_coach_armor_max_value<br>stage_coach_armor_min_value<br>stage_coach_wheels_default_value<br>stage_coach_wheels_max_value<br>stage_coach_wheels_min_value<br>torch_default_value<br>torch_drain_between_nodes<br>torch_max_value<br>torch_min_value<br></details>|Yes||
|multiply_stat|Example: `multiply_stat,torch_drain_between_nodes,-0.33,`<br>Slot 1 values:<br>torch_drain_between_nodes|Yes||
|multiply_stats|-1.00...3.00|Yes||
|sub_stat|Example: `sub_stat,map_generation_node_spawn_multiplier,Store,2,`<br>Slot 1 values:<br><details><summary>Click&#8201;to&#8201;expand</summary>battle_configuration_chance<br>item_max_qty<br>loot_chance<br>loot_qty<br>map_generation_node_execute_loot_chance<br>map_generation_node_filler_limit_modifier<br>map_generation_node_spawn_multiplier<br>map_generation_route_chance_multiplier<br>resistance<br>route_effect_apply_multiplier<br>run_generation_typical_biome_chance<br>score_penalty_multiplier<br>scout_node_chance<br>scout_route_chance<br>store_cost_buy_multiplier<br>torch_remove_percent</details><br>Slot 2 values:<br><details><summary>Click&#8201;to&#8201;expand</summary>BAUBLES_QTY<br>BONUS_CREATURE_DEN_REWARDS<br>BOTTLE_CASE_QTY<br>BeastmenAlpha<br>BossSelect<br>CHIRURGEONS_MAP_QTY<br>COMPRESS_KIT_QTY<br>COVEN_CAULDRON<br>Cache<br>City<br>Coast<br>CovenAssist<br>CreatureDen<br>Dungeon<br>FOOD_QTY<br>Farm<br>Forest<br>GauntChirurgeon<br>Guardian<br>HOARDERS_MAP_QTY<br>Hospital<br>INN_KINGDOM_COMBAT_ITEM_PULLS<br>INN_KINGDOM_FOOD_PULLS<br>INN_KINGDOM_INN_ITEM_PULLS<br>INN_KINGDOM_SC_ITEM_PULLS<br>INN_KINGDOM_TRINKET_PULLS<br>INN_KINGDOM_WHISKEY_PULLS<br>Inn<br>KINGDOM_CHAMPS<br>KingdomBoss<br>KingdomCamp<br>KingdomInn<br>KingdomInnSieged<br>MATERIALS_QTY<br>MEDICINE_CHEST_QTY<br>Oasis<br>PRODUCTION_CHC<br>RELICS_QTY<br>ROAD_DEBRIS_CHC<br>Store<br>StoryAssist<br>StoryCosmic<br>StoryCultist<br>StoryHero<br>StoryResist<br>TRINKET_CHC<br>Warlord<br>WatchTower<br>actor_path_change<br>bandages<br>biome_bosses_cleared<br>candles<br>combat<br>concoction<br>contraption<br>death<br>doom<br>driving<br>explosive<br>faction<br>food<br>gold<br>hazard<br>inn_health_heal<br>inn_wainwright<br>inn_wound_heal<br>lock_positive_quirk<br>memory<br>oblivion_tear<br>optional_biomes_cleared<br>poultice<br>powder<br>remove_disease<br>remove_negative_quirk<br>rest<br>restorative<br>rough_patch<br>route_catacombs_combat_faction<br>route_caves_combat_faction<br>route_city_combat_gaunt<br>route_city_combat_military<br>route_coast_combat_faction<br>route_coast_combat_gaunt<br>route_coast_combat_military<br>route_farm_combat_gaunt<br>route_farm_combat_military<br>route_forest_combat_faction<br>route_forest_combat_gaunt<br>route_forest_combat_military<br>route_tundra_combat_gaunt<br>safe<br>stage_coach_upgrade<br>trap<br>trinket<br>typical_biomes_cleared<br>wandering<br>whiskey</details>|Yes||

</details>

<details>
<summary>RunGoal</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |No||
|any_conditions|Condition&nbsp;ID |Yes||
|generation_all_conditions|Condition&nbsp;ID |Yes||
|m_ActorClassIds|<sub>parse fail</sub>|No||
|m_Chance|1...1|No||
|m_CompletionLimit|-1...1|No||
|m_GoalIconOverride|candle_item<br>rest<br>trinket|No||
|m_GoalTooltipLocKeyOverride|goal_candle_reward_1_tooltip<br>goal_candle_reward_2_tooltip<br>goal_candle_reward_4_tooltip|No||
|m_LootTableId|LootTable&nbsp;ID |No||
|m_RunGoalCategoryId|RunGoalCategory&nbsp;ID |No||
|m_Score|1...4|No||

</details>

<details>
<summary>RunGoalCategory</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_PrerequisiteRunGoalCategoryId|<sub>parse fail</sub>|No||

</details>

<details>
<summary>RunLevel</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_NumberOfTypicalBiomesMax|1...3|No||
|m_NumberOfTypicalBiomesMin|1...4|No||
|m_UnlockId|<sub>parse fail</sub>|No||

</details>

<details>
<summary>RunValueLevel</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_IsPercent|Boolean|No||
|m_IsVisible|Boolean|No||
|m_Max|0...5|No||
|m_Min|0...3|No||
|m_RunValueType|escalation<br>stage_coach_armor<br>stage_coach_wheels|No||
|m_Tags|Tags|No||

</details>

<details>
<summary>RunValueTransaction</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_RunValueType|stage_coach_armor<br>stage_coach_wheels|No||
|m_StoreCostMultiplierId|NarrationType&nbsp;ID |No||
|m_TransactionAmount|1...4|No||
|m_isDiscounted|Boolean|No||

</details>

<details>
<summary>SkillBlock</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|effect_skill_attribute_tags|Tags|Yes||
|m_PerformerSkillTags|heal<br>melee<br>ranged<br>stress_heal|No||
|m_TargetSkillTags|Tags|No||

</details>

<details>
<summary>SkillModifier</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|effects|Effect&nbsp;ID |Yes||
|m_Chance|0.50...1.00|No||
|m_IsForceEquip|Boolean|No||
|m_Tags|Tags|No||

</details>

<details>
<summary>SkillReplacement</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_FromActorDataSkillId|ActorDataSkill&nbsp;ID |No||
|m_IsPathComparisonValid|Boolean|No||
|m_ToActorDataSkillId|ActorDataSkill&nbsp;ID |No||

</details>

<details>
<summary>SkillSet</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_IsDefault|Boolean|No||
|skills|ActorDataSkill&nbsp;ID |Yes||

</details>

<details>
<summary>StageCoachSkin</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_UnlockId|Unlock&nbsp;ID |No||

</details>

<details>
<summary>StoryAlignment</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_DisharmoniousAlignments|StoryAlignment&nbsp;ID |Yes||
|m_HarmoniousAlignments|StoryAlignment&nbsp;ID |Yes||

</details>

<details>
<summary>StoryChoice</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |Yes||
|m_AlignmentId|StoryAlignment&nbsp;ID |No||
|m_AnyTags|Tags|Yes||
|m_Chance|0...9999|No||
|m_CostId|Cost&nbsp;ID |No||
|m_DrawTags|Tags|Yes||
|m_EnemyStoryChoicePreviewIds|icon_blight_Preview<br>icon_debuff_Preview<br>icon_move_Preview<br>icon_story_token_blind-line_Preview<br>icon_story_token_combo_Preview<br>icon_story_token_daze_Preview<br>icon_story_token_strength_Preview<br>icon_story_token_vulnerable_Preview|Yes||
|m_EnemyStoryChoicePreviewShowNumbers|Boolean|Yes||
|m_EnemyStoryChoicePreviewValues|0...1000|Yes||
|m_ExclusiveTags|Tags|No||
|m_PlayerStoryChoicePreviewIds|<details><summary>Click&#8201;to&#8201;expand</summary>icon_buff_Preview<br>icon_story_ancestor_Preview<br>icon_story_armor_Preview<br>icon_story_avoid_Preview<br>icon_story_books_Preview<br>icon_story_buff_Preview<br>icon_story_candle_loot_Preview<br>icon_story_coach_upgrade_loot_Preview<br>icon_story_combat_Preview<br>icon_story_combat_item_loot_Preview<br>icon_story_courtier_Preview<br>icon_story_coven_Preview<br>icon_story_food_large_Preview<br>icon_story_food_loot_Preview<br>icon_story_food_med_Preview<br>icon_story_health_heal_Preview<br>icon_story_materials_Preview<br>icon_story_mystery_treasure_loot_Preview<br>icon_story_quirk_mixed_Preview<br>icon_story_quirk_negative_Preview<br>icon_story_quirk_positive_Preview<br>icon_story_relic_large_Preview<br>icon_story_relic_loot_Preview<br>icon_story_rest_loot_Preview<br>icon_story_scouting_Preview<br>icon_story_signature_inn_loot_Preview<br>icon_story_stress_dmg_Preview<br>icon_story_stress_heal_Preview<br>icon_story_stress_mixed_Preview<br>icon_story_supplies_med_Preview<br>icon_story_supplies_small_Preview<br>icon_story_team_buff_Preview<br>icon_story_team_health_heal_Preview<br>icon_story_team_stress_heal_Preview<br>icon_story_team_token_block_Preview<br>icon_story_team_token_crit_Preview<br>icon_story_team_token_dodge+_Preview<br>icon_story_team_token_strength_Preview<br>icon_story_token_block_Preview<br>icon_story_token_crit_Preview<br>icon_story_token_daze_Preview<br>icon_story_token_speed_Preview<br>icon_story_token_stealth_Preview<br>icon_story_token_strength_Preview<br>icon_story_token_taunt_Preview<br>icon_story_token_vulnerable_Preview<br>icon_story_token_weak_Preview<br>icon_story_torch_Preview<br>icon_story_treasure_large<br>icon_story_trinket_loot_Preview<br>icon_story_wheel_Preview<br>icon_story_wine_Preview<br></details>|Yes||
|m_PlayerStoryChoicePreviewShowNumbers|Boolean|Yes||
|m_PlayerStoryChoicePreviewValues|-25...1000|Yes||
|m_ProgressGroupId|base_story<br>dlc_story|No||
|m_ResultActorClassId|<sub>parse fail</sub>|No||
|m_ResultAudioOverrideId|caretaker|No||
|m_ResultBattleConfigurationId|BattleConfiguration&nbsp;ID |No||
|m_ResultBattleConfigurationTableId|BattleConfigurationTable&nbsp;ID |No||
|m_ResultLootIds|LootTable&nbsp;ID |Yes||
|m_ResultType|COMBAT<br>DRIVING<br>UI|No||
|m_ScoutDist|20...20|No||
|m_ScoutPercent|1...1|No||

</details>

<details>
<summary>StoryChoiceReplacement</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_FromDrawTags|Tags|No||
|m_RemoveDrawTags|Tags|No||
|m_ToDrawTags|Tags|No||

</details>

<details>
<summary>StoryDataEffects</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|enemy_actor_effects|Effect&nbsp;ID |Yes||
|party_actor_combat_effects|Effect&nbsp;ID |Yes||
|party_actor_effects|Effect&nbsp;ID |Yes||
|selection_actor_combat_effects|Effect&nbsp;ID |Yes||
|selection_actor_effects|Effect&nbsp;ID |Yes||

</details>

<details>
<summary>StressTrigger</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |No||
|m_Chance|0.00...1.00|No||
|m_FilterId|Objects<br>hazard<br>rough_patch<br>safe|No||
|m_QueueFailedPresentationChance|0.65...1.00|No||
|m_RoleType|OBSERVING_PERFORMER<br>OBSERVING_TARGET<br>PARTY<br>PERFORMER<br>TARGET|No||
|m_Stress|-1...2|No||
|m_TriggerLimit|1...1|No||
|m_Type|crit<br>death<br>deaths_door<br>node_path_taken<br>pet_inspect<br>road_event_completed|No||

</details>

<details>
<summary>SummonControllerConfiguration</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ShowWaveProgress|Boolean|No||
|sequence|SummonSequenceElement&nbsp;ID |Yes||

</details>

<details>
<summary>SummonSequenceElement</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |Yes||
|m_ActorClassId|<sub>parse fail</sub>|No||
|m_IfRoom|Boolean|No||
|m_LocationType|BACK<br>FRONT<br>RANDOM|No||

</details>

<details>
<summary>Token</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|consume_buffs|<sub>parse fail</sub>|No||
|m_AlwaysRemove|Boolean|No||
|m_Chance|0.50...1.00|No||
|m_ConditionId|Condition&nbsp;ID |No||
|m_ConsumeLimit|1...1|No||
|m_ConsumePriority|1...2|No||
|m_ConsumeTypes|delay_turn<br>evade<br>forced_target<br>manual<br>passive<br>round_end_buff<br>skill_calculate_damage_buff<br>skill_damage_buff<br>skip_turn|No||
|m_DurationAmount|0...10|No||
|m_DurationIsSingleRemove|Boolean|No||
|m_DurationType|combat_end<br>every_turn_start<br>infinite<br>performer_turn_end<br>performer_turn_start<br>round_end<br>round_start|No||
|m_InvertTokenId|Token&nbsp;ID |No||
|m_IsExclusiveSource|Example: `m_IsExclusiveSource,True,token,`<br>Slot 2 values:<br>token|Yes||
|m_IsHidden|Boolean|No||
|m_IsPerformer|Boolean|No||
|m_IsRankToken|Boolean|No|Only adds a square bracket indicator under this token's icon, doesn't have gameplay effects|
|m_IsRemovedOnSourceCapture|Boolean|No||
|m_IsRemovedOnSourceDeath|Boolean|No||
|m_IsTarget|Boolean|No||
|m_Limit|1...10|No||
|m_NegateAllIds|Token&nbsp;ID |No||
|m_NegateIds|Token&nbsp;ID |Yes||
|m_PreviewValidStatuses|<sub>parse fail</sub>|No||
|m_RemoveTypes|guarding<br>on_damaging_blocked<br>on_damaging_miss<br>on_killed<br>on_non_damaging_hit<br>on_non_damaging_miss|Yes||
|m_ShowCombatDuration|Boolean|No||
|m_ShowConsumePopText|Boolean|No||
|m_ShowDescription|Boolean|No||
|m_ShowName|Boolean|No||
|m_Tags|Tags|Yes||
|m_TeamLimit|2...2|No||
|m_TokenGlossaryAlwaysDisplay|Boolean|No||
|m_TokenGlossaryBiomeTag|Tags|No||
|m_TokenGlossaryHeroTag|Tags|No||
|m_TokenGlossaryPathTag|Tags|Yes||
|m_TokenGlossaryTagDisplay|Tags|Yes||
|remove_any_conditions|Condition&nbsp;ID |No||
|replace|WITH|Yes||

</details>

<details>
<summary>TokenIgnore</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|all_conditions|Condition&nbsp;ID |Yes||
|any_conditions|Condition&nbsp;ID |Yes||
|m_IgnoredTokenIds|Token&nbsp;ID |Yes||
|m_IgnoredTokenTypes|forced_target|No||
|m_IsInstanceAddedToPerformer|Boolean|No||
|m_IsInstanceAddedToTarget|Boolean|No||
|m_IsInstanceSourcePerformer|Boolean|No||
|m_IsInstanceSourceTarget|Boolean|No||
|m_IsVisible|Boolean|No||

</details>

<details>
<summary>TorchLevel</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Tags|Tags|Yes||
|m_TorchMax|0...100|No||
|m_TorchMin|0...76|No||

</details>

<details>
<summary>TorchLevelGroup</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|torch_levels|TorchLevel&nbsp;ID |Yes||

</details>

<details>
<summary>TorchTrigger</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Tags|Tags|No||
|m_TorchChange|-5...-5|No||
|m_Type|DEATH|No||

</details>

<details>
<summary>TrinketSet</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ExternalBuffsId|speed_increase_trinket|No||

</details>

<details>
<summary>Unlock</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_CostId|Cost&nbsp;ID |No||
|m_RequirementIds|<sub>parse fail</sub>|No||

</details>

<details>
<summary>UnlockTable</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|cost|Example: `cost,char_cosmetics_price_1,0,0.166666666666667,`<br>Slot 1 values:<br><details><summary>Click&#8201;to&#8201;expand</summary>char_cosmetics_price_1<br>char_cosmetics_price_2<br>char_cosmetics_price_3<br>char_cosmetics_price_4<br>char_cosmetics_price_5<br>char_cosmetics_price_6<br>combat_items_price_1<br>combat_items_price_2<br>combat_items_price_3<br>inn_items_price_1<br>inn_items_price_2<br>inn_items_price_3<br>stagecoach_price_1<br>stagecoach_price_2<br>stagecoach_price_3<br>trinket_price_1<br>trinket_price_2<br>trinket_price_3</details>|Yes||
|m_ProgressGroupId|base_cosmetic<br>base_item<br>dlc_cosmetic|No||
|m_chances|1...1|Yes||
|m_ids|Unlock&nbsp;ID |Yes||
|m_types|unlock|Yes||

</details>

<details>
<summary>UnlockTrack</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_ProgressGroupId|dlc|No||
|unlocks|<sub>parse fail</sub>|Yes||

</details>

<details>
<summary>WoundTrigger</summary>

| Field | Values | Multiple Values | Comment |
| :---- | :----- | :-------------- | :------ |
|m_Chance|0.03...1.00|No||
|m_ConditionId|Condition&nbsp;ID |No||
|m_InputMin|1...1|No||
|m_InputType|kingdom_day|No||
|m_SourceId|Overstress&nbsp;ID |No||
|m_Type|deaths_door<br>inn_start<br>overstress|No||
|m_WoundPercentChange|-0.15...0.20|No||
|m_WoundPercentMax|0.19...0.19|No||

</details>

