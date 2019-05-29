Feature: celestial_rootfs_install

    Scenario: update rootfs device node with expected fs format
        Given an ext4 formatted rootfs file
        And a target device node
        And we expect rootfs format ext4
        When we invoke celestial_rootfs_install
        Then the ext3 file is burned into the target device node

    Scenario: faults when given an improperly formatted file
        Given an ext2 formatted rootfs file
        And we expect rootfs format ext4
        When we invoke celestial_rootfs_install
        Then celestial_rootfs_install fails with ValueError
